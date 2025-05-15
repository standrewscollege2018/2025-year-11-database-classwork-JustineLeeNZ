''' run queries on student database - format results in columns - Justine Lee '''

# import sqlite3 library
import sqlite3

# define database to use
DATABASE = 'student_info.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# select all names from student database
cursor.execute("SELECT first_name, last_name, tutor FROM student ORDER BY student_id")
student_details = cursor.fetchall()


# display info about selected students
# heading row
print(f"{'First name':15} {'Last name':20} {'Tutor':5}")
print("="*42)

# info about each student
for detail in student_details:
    print(f"{detail[0]:15} {detail[1]:20} {detail[2]:5}")



