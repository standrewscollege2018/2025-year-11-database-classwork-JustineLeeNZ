''' run queries on student database with more than 1 user input - Justine Lee '''

# import sqlite3 library
import sqlite3

# define database to use
DATABASE = 'student_info.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# ask user to enter a name to search for
letter = input("Enter first letter of last name: ")

# add wildcard characters % to end of letter that user entered - THIS IS THE PRESET VALUE FOR THE QUERY
letter = letter + "%"

# ask user to enter age to search for
age = int(input("Enter minimum age: "))

# select all names from student database that match the starting letter and age entered by the user
cursor.execute("SELECT first_name, last_name, age FROM student WHERE age > ? AND last_name LIKE ?", (age,letter))
results = cursor.fetchall()

# display info about student(s) whose name and age matches what the user entered
for student in results:
    # name
    print(f"\nName: {student[0]} {student[1]}")
    # age
    print(f"Age: {student[2]}")




