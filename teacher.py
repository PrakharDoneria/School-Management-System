import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def add_teacher(name):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Add a new teacher
        cursor.execute("INSERT INTO teachers (name) VALUES (%s)", (name,))

        print(f"Added new teacher: {name}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Commit changes and close connection
        db_connection.commit()
        cursor.close()
        db_connection.close()

def remove_teacher(teacher_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Remove a teacher by ID
        cursor.execute("DELETE FROM teachers WHERE id = %s", (teacher_id,))

        print(f"Removed teacher with ID {teacher_id}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Commit changes and close connection
        db_connection.commit()
        cursor.close()
        db_connection.close()

if __name__ == "__main__":
    teacher_name = input("Enter Teacher Name: ")
    add_teacher(teacher_name)

    teacher_id_to_remove = input("Enter Teacher ID to Remove: ")
    remove_teacher(teacher_id_to_remove)
