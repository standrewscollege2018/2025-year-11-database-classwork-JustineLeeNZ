''' run queries on student database with user input - Justine Lee '''

# import sqlite3 library
import sqlite3

# define database to use
DATABASE = 'student_info.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# select all names from student database
cursor.execute("SELECT student_id, first_name, last_name FROM student ORDER BY student_id")
results = cursor.fetchall()

# display student names as numbered list using primary key
for result in results:
    name = f" {result[1]} {result[2]}"
    print(f"{result[0]:3} {name:}")

# get number of student to display
selection = int(input("\nEnter the number of selected student: "))

# get details of selected student
cursor.execute("SELECT * FROM student WHERE student_id = ?", (selection,))
details = cursor.fetchall()
# display info about selected student
for detail in details:
    # name
    print(f"Name: {detail[1]} {detail[2]}")
    # age
    print(f"Age: {detail[3]}")
    # tutor
    print(f"Tutor: {detail[5]}")



