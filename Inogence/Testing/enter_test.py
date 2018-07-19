import sqlite3

# CAN/BREBEUF/402/ENG-29/Jul/2018/15:00

db_schedule = sqlite3.connect("schedule.db")
cursor = db_schedule.cursor()

exam_id = ''
country = input("Country? ")
exam_id += country
school = input("School?")
