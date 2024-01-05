import mysql.connector
import json

def connect_to_database():
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="school_management"
    )

def backup_data():
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Fetch all teacher data
        cursor.execute("SELECT * FROM teachers")
        teacher_data = cursor.fetchall()

        if not teacher_data:
            print("No data to backup.")
            return

        # Convert data to JSON format
        backup_file = "backup_data.json"
        with open(backup_file, 'w') as file:
            data_to_backup = []
            for teacher_info in teacher_data:
                data_to_backup.append({
                    "id": teacher_info[0],
                    "name": teacher_info[1],
                    "present_days": teacher_info[2],
                    "half_days": teacher_info[3],
                    "absent_days": teacher_info[4],
                    "salary": teacher_info[5]
                })

            json.dump(data_to_backup, file, indent=2)

        print(f"Data backed up successfully to {backup_file}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close connection
        cursor.close()
        db_connection.close()

# Example usage
if __name__ == "__main__":
    backup_data()
