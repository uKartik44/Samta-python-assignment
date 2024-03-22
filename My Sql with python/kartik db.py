import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123password",
    database="kartikdb"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


# Insert a new student record
sql_insert = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
student_data = ("Alice", "Smith", 18, 95.5)
mycursor.execute(sql_insert, student_data)
mydb.commit()

# Update the grade of the student with first name "Alice"
sql_update = "UPDATE students SET grade = %s WHERE first_name = %s"
update_data = (97.0, "Alice")
mycursor.execute(sql_update, update_data)
mydb.commit()

# Delete the student with last name "Smith"
sql_delete = "DELETE FROM students WHERE last_name = %s"
delete_data = ("Smith",)
mycursor.execute(sql_delete, delete_data)
mydb.commit()

# Fetch and display all student records
mycursor.execute("SELECT * FROM students")
students = mycursor.fetchall()
for student in students:
    print(student)

# Close the database connection
mydb.close()

