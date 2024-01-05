import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="prakhardoneria",
        password="jinga la hu hu",
        database="school_management"
    )

def calculate_presence_percentage(teacher_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Get total days (present + half + absent)
        cursor.execute("SELECT present_days, half_days, absent_days FROM teachers WHERE id = %s", (teacher_id,))
        present_days, half_days, absent_days = cursor.fetchone()

        total_days = present_days + half_days + absent_days

        # Calculate percentage
        if total_days == 0:
            percentage = 0.0
        else:
            percentage = (present_days / total_days) * 100

        print(f"Teacher ID {teacher_id} has a presence percentage of {percentage:.2f}%")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close connection
        cursor.close()
        db_connection.close()


if __name__ == "__main__":
    teacher_id = input("Enter Teacher ID: ")
    calculate_presence_percentage(teacher_id)
