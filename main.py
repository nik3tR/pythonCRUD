import psycopg2 

# connect to my local postgres DB
conn = psycopg2.connect(database="studentsA3",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5433")

db = conn.cursor()

# select all students from my table
def getAllStudents():
    db.execute("SELECT * FROM students")

    #pretty printing
    rows = db.fetchall()
    for row in rows:
        print(row)

# insert passed values into a new student in the table
def addStudent(first_name, last_name, email, enrollment_date):
 db.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s);
            """, (first_name, last_name, email, enrollment_date))

# update email of a student with a given ID
def updateStudentEmail(student_id, new_email):
    db.execute("""UPDATE students 
                    SET email = %s
                    WHERE id = %s""", (new_email, student_id))

# remove row with a given student ID
def deleteStudent(student_id):
    db.execute(f"DELETE FROM students WHERE id = {student_id}")


def main():
    
    #simple loop to choose what function to run
    while True:
        print("\nChoose an option:")
        print("1. Get all students")
        print("2. Add a new student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")
    
        choice = input("Enter: ")

        if choice == "1":
            getAllStudents()

        elif choice == "2":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Email: ")
            enrollment_date = input("Enter Enrol Date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)

        elif choice == "3":
            student_id = input("enter ID to update: ")
            email = input("enter updated email: ")
            updateStudentEmail(student_id, email)

        elif choice == "4":
            student_id = input("enter ID to vaporize: ")
            deleteStudent(student_id)

        elif choice == "5":
            conn.commit()
            db.close()
            conn.close()
            break

if __name__ == "__main__":
    main()

