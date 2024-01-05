import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def mark_attendance(teacher_id, status):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Validate status input
        if status.lower() not in ['absent', 'present']:
            print("Invalid attendance status. Please enter 'absent' or 'present'.")
            return

        # Update attendance based on status
        if status.lower() == 'absent':
            cursor.execute("UPDATE teachers SET absent_days = absent_days + 1 WHERE id = %s", (teacher_id,))
        elif status.lower() == 'present':
            cursor.execute("UPDATE teachers SET present_days = present_days + 1 WHERE id = %s", (teacher_id,))

        print(f"Attendance marked for Teacher ID {teacher_id}: {status}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Commit changes and close connection
        db_connection.commit()
        cursor.close()
        db_connection.close()

if __name__ == "__main__":
    teacher_id = input("Enter Teacher ID: ")
    status = input("Enter Attendance Status (absent/present): ")
    mark_attendance(teacher_id, status)
