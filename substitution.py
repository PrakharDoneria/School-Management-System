import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="prakhardoneria",
        password="kise_ko_batana_mt",
        database="school_management"
    )

def substitute_teacher(substitute_id, replaced_id):
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Get teacher names for substitution
        cursor.execute("SELECT name FROM teachers WHERE id IN (%s, %s)", (substitute_id, replaced_id))
        teacher_names = cursor.fetchall()

        substitute_name, replaced_name = teacher_names

        # Perform substitution
        cursor.execute("UPDATE teachers SET name = %s WHERE id = %s", (substitute_name, replaced_id))
        cursor.execute("DELETE FROM teachers WHERE id = %s", (substitute_id))

        print(f"Substituted {substitute_name} with {replaced_name} successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Commit changes and close connection
        db_connection.commit()
        cursor.close()
        db_connection.close()

# Example usage
if __name__ == "__main__":
    substitute_teacher(2, 1)
