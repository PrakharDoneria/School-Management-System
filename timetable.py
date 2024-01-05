import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def add_or_update_timetable():
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Get teacher ID and substitute ID for the timetable
        teacher_id = input("Enter Teacher ID for the timetable: ")
        substitute_id = input("Enter Substitute Teacher ID if any (or press Enter to skip): ")

        # Check if the teacher exists
        cursor.execute("SELECT * FROM teachers WHERE id = %s", (teacher_id,))
        teacher_exists = cursor.fetchone()

        if not teacher_exists:
            print(f"Teacher with ID {teacher_id} does not exist.")
            return

        # Update timetable with teacher and substitute information
        cursor.execute("INSERT INTO timetable (teacher_id, substitute_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE substitute_id = %s",
                       (teacher_id, substitute_id, substitute_id))

        print("Timetable updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Commit changes and close connection
        db_connection.commit()
        cursor.close()
        db_connection.close()


if __name__ == "__main__":
    add_or_update_timetable()
