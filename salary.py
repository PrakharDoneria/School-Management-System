import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def calculate_salary(teacher_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Get teacher information
        cursor.execute("SELECT present_days, half_days, absent_days FROM teachers WHERE id = %s", (teacher_id,))
        present_days, half_days, absent_days = cursor.fetchone()

        # Calculate total salary with deductions
        salary_per_day = 1000  # Adjust as needed
        deduction_per_half_day = 500  # Adjust as needed

        total_salary = (present_days * salary_per_day) - (half_days * deduction_per_half_day)

        print(f"Teacher ID {teacher_id} has a total salary of {total_salary} with deductions for absent and half-days.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close connection
        cursor.close()
        db_connection.close()


if __name__ == "__main__":
    teacher_id = input("Enter Teacher ID: ")
    calculate_salary(teacher_id)
