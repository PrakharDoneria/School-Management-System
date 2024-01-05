import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def mark_half_day(teacher_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Update half-days count
        cursor.execute("UPDATE teachers SET half_days = half_days + 1 WHERE id = %s", (teacher_id,))

        print(f"Marked half-day for Teacher ID {teacher_id}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Commit changes and close connection
        db_connection.commit()
        cursor.close()
        db_connection.close()


if __name__ == "__main__":
    teacher_id = input("Enter Teacher ID: ")
    mark_half_day(teacher_id)
