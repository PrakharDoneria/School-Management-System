import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def modify_teacher_information(teacher_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Get current information about the teacher
        cursor.execute("SELECT * FROM teachers WHERE id = %s", (teacher_id,))
        current_info = cursor.fetchone()

        if not current_info:
            print(f"Teacher with ID {teacher_id} not found.")
            return

        print("Current Teacher Information:")
        print(f"ID: {current_info[0]}")
        print(f"Name: {current_info[1]}")
        print(f"Present Days: {current_info[2]}")
        print(f"Half Days: {current_info[3]}")
        print(f"Absent Days: {current_info[4]}")
        print(f"Salary: {current_info[5]}")

        # Update teacher information
        new_name = input("Enter new name (press Enter to keep current name): ")
        new_present_days = int(input("Enter new present days (press Enter to keep current days): ") or current_info[2])
        new_half_days = int(input("Enter new half days (press Enter to keep current days): ") or current_info[3])
        new_absent_days = int(input("Enter new absent days (press Enter to keep current days): ") or current_info[4])

        cursor.execute("UPDATE teachers SET name = %s, present_days = %s, half_days = %s, absent_days = %s WHERE id = %s",
                       (new_name, new_present_days, new_half_days, new_absent_days, teacher_id))

        print("Teacher information updated successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Commit changes and close connection
        db_connection.commit()
        cursor.close()
        db_connection.close()

# Example usage
if __name__ == "__main__":
    teacher_id_to_modify = input("Enter Teacher ID to Modify: ")
    modify_teacher_information(teacher_id_to_modify)
