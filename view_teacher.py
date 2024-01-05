import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def view_teacher_information(teacher_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Get detailed information about the teacher
        cursor.execute("SELECT * FROM teachers WHERE id = %s", (teacher_id,))
        teacher_info = cursor.fetchone()

        if not teacher_info:
            print(f"Teacher with ID {teacher_id} not found.")
            return

        print("Teacher Information:")
        print(f"ID: {teacher_info[0]}")
        print(f"Name: {teacher_info[1]}")
        print(f"Present Days: {teacher_info[2]}")
        print(f"Half Days: {teacher_info[3]}")
        print(f"Absent Days: {teacher_info[4]}")
        print(f"Salary: {teacher_info[5]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close connection
        cursor.close()
        db_connection.close()

# Example usage
if __name__ == "__main__":
    teacher_id = input("Enter Teacher ID: ")
    view_teacher_information(teacher_id)
