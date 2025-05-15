import sqlite3

DATABASE = "student_info.db"

connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()

cursor.execute("SELECT * FROM student")

results = cursor.fetchall()

for result in results:
    print(result)