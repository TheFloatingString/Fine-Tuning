import sqlite3

db = sqlite3.connect("results.db")
cursor = db.cursor()


def enter_data(user_id_, test_id, grade, verbose=False):
    """Function to enter data"""

    # call global variables
    global db
    global cursor

    # save to SQLite database
    cursor.execute('''INSERT INTO users(user_id, test_id, grade)
                      VALUES(?, ?, ?)''',
                      (user_id_, test_id, grade))
    db.commit()
    if verbose:
        print("Commit successful!")


def return_data_results(column_name, key):
    """Function to return data based on unique key from column_name"""

    # call global variables
    global db
    global cursor

    cursor.execute("SELECT user_id, test_id, grade FROM users WHERE {}=?".format(column_name), (key,))
    user = cursor.fetchall()
    for row in user:
        print(row)

    return user


if __name__ == '__main__':
    cursor.execute('''DELETE FROM users WHERE test_id = ? ''', ('CAN/BREBEUF/402/ENG-29/Jul/2018/15:00',))
    db.commit()
    enter_data('1', "CAN/BREBEUF/402/ENG-29/Jul/2018/15:00", 75.0)
    return_data_results("user_id", "1")
