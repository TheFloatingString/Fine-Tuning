import sqlite3
from datetime import datetime

db = sqlite3.connect("database.db")
cursor = db.cursor()

# cursor.execute(''' CREATE TABLE users(user_id TEXT, date_and_time TEXT, activity TEXT, intensity REAL, test_id TEXT , notes TEXT)''')


user_id_ = '1'
date_and_time_ = "17/Jul/2018/19:00"+'-'+"17/Jul/2018/20:00"
activity_ = 'study'
intensity_ = 9.0
test_id_ = "CAN/BREBEUF/402/ENG"+'-'+"19/Jul/2018/15:00"
notes_ = "Studied with music"

cursor.execute('''INSERT INTO users(user_id, date_and_time, activity, intensity, test_id, notes)
                  VALUES(?, ?, ?, ?, ?, ?)''',
                  (user_id_, date_and_time_, activity_, intensity_, test_id_, notes_))

db.commit()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)
