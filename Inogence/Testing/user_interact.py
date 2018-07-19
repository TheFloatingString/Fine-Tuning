import sqlite3
from quick_scripting import return_data_results
from datetime import datetime
from datetime import timedelta

from sklearn.ensemble import ExtraTreesClassifier


# Connect to SQLite database
db = sqlite3.connect("database.db")
cursor = db.cursor()


python_study_db = []        # list of Python study database


def enter_data(user_id_, date_and_time_, activity_, intensity_, test_id_, notes_, verbose=False):
    """Function to enter data"""

    # call global variables
    global db
    global cursor

    # save to SQLite database
    cursor.execute('''INSERT INTO users(user_id, date_and_time, activity, intensity, test_id, notes)
                      VALUES(?, ?, ?, ?, ?, ?)''',
                      (user_id_, date_and_time_, activity_, intensity_, test_id_, notes_))
    db.commit()
    if verbose:
        print("Commit successful!")


def return_data_user(column_name, key):
    """Function to return data based on unique key from column_name"""

    # call global variables
    global db
    global cursor

    cursor.execute("SELECT user_id, date_and_time, activity, intensity, test_id, notes FROM users WHERE {}=?".format(column_name), (key,))
    user = cursor.fetchall()
    for row in user:
        print(row)

    return user


user_db_raw = return_data_user("user_id", "1")
results_db_raw = return_data_results("user_id", "1")

# processing for test scores
list_of_test_id = []
test_scores = []
for row in results_db_raw:
    list_of_test_id.append(row[1])
    test_scores.append(row[2])

# raw_test = user_db_raw[0][4].split('-')

# test information
# test_id = raw_test[0]
# test_date = datetime.strptime(raw_test[1], "d/b/Y/H:M")


X = []      # ensemble of data for studying a test

print("\n\n\n")
# access study information
for test in list_of_test_id:

    X_unique_test = []          # data for a unique test
    total_time_studied = 0.0    # time studied
    total_avg_intensity = 0.0   # average intensity

    num_study_sessions = 0     # number of study sessions

    # retain only sessions for that particular test ID
    total_sessions = [t for t in user_db_raw if t[4] == test]

    for session in total_sessions:
        # if activity is studying
        if session[2] == "study":
            print(session)
            print('***')
            num_study_sessions += 1
            # compute study time
            time_studied_total = session[1].split('-')
            start_time = datetime.strptime(time_studied_total[0], "%d/%b/%Y/%H:%M")
            end_time = datetime.strptime(time_studied_total[1], "%d/%b/%Y/%H:%M")
            elapsed_time = end_time - start_time
            time_studied = elapsed_time/timedelta(minutes=1)

            # add to total
            total_time_studied += time_studied


            # compute intensity time
            total_avg_intensity += session[3]



    print(total_avg_intensity)
    print(len(total_sessions))
    total_avg_intensity /= num_study_sessions

    X.append([total_time_studied, total_avg_intensity])


for row, score in zip(X, test_scores):
    print(row, score)

# importance of scores
model = ExtraTreesClassifier()
model.fit(X, test_scores)
values = model.feature_importances_
index_list = ['Study duration', 'Study intensity']
dict_of_importance = dict(zip(index_list, values))
print(dict_of_importance)
