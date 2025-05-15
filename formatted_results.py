''' run queries on student database - basic formatiing of results - Justine Lee '''

# import sqlite3 library
import sqlite3

# define database to use
DATABASE = 'student_info.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# select all names from student database
cursor.execute("SELECT * FROM student ORDER BY student_id")
student_details = cursor.fetchall()


# display info about selected students
for detail in student_details:
    # name
    print(f"Name: {detail[1]} {detail[2]}")
    # age
    print(f"Age: {detail[3]}")
    # tutor
    print(f"Tutor: {detail[5]}\n")



