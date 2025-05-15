''' run queries on student database with user input and preset values - Justine Lee '''

# import sqlite3 library
import sqlite3

# define database to use
DATABASE = 'student_info.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# ask user to enter a name to search for
search = input("Enter a student name to search for: ")

# add wildcard characters % to beginning and end of name that user entered - THIS IS THE PRESET VALUE FOR THE QUERY
search = "%" + search + "%"

# select all names from student database that match the name entered by the user
cursor.execute("SELECT * FROM student WHERE first_name LIKE ?", (search,))
results = cursor.fetchall()

# display info about student(s) whose name matches what the user entered
for student in results:
    # name
    print(f"\nName: {student[1]} {student[2]}")
    # age
    print(f"Age: {student[3]}")
    # tutor
    print(f"Tutor: {student[5]}")



