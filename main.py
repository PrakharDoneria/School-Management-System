import mysql.connector
from substitution import substitute_teacher
from attendance import mark_attendance
from half_day import mark_half_day
from percentage import calculate_presence_percentage
from teacher import add_teacher, remove_teacher
from salary import calculate_salary

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="prakhardoneria",
        password="kise_ko_batana_mt",
        database="school_management"
    )

def display_menu():
    print("School Management System Menu:")
    print("1. Substitute Teacher")
    print("2. Mark Attendance")
    print("3. Mark Half Day")
    print("4. Calculate Presence Percentage")
    print("5. Add Teacher")
    print("6. Remove Teacher")
    print("7. Calculate Salary")
    print("8. Exit")

def main():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            substitute_teacher(2, 1)
        elif choice == "2":
            teacher_id = input("Enter Teacher ID: ")
            status = input("Enter Attendance Status (absent/present): ")
            mark_attendance(teacher_id, status)
        elif choice == "3":
            teacher_id = input("Enter Teacher ID: ")
            mark_half_day(teacher_id)
        elif choice == "4":
            teacher_id = input("Enter Teacher ID: ")
            calculate_presence_percentage(teacher_id)
        elif choice == "5":
            name = input("Enter Teacher Name: ")
            add_teacher(name)
        elif choice == "6":
            teacher_id = input("Enter Teacher ID to Remove: ")
            remove_teacher(teacher_id)
        elif choice == "7":
            teacher_id = input("Enter Teacher ID: ")
            calculate_salary(teacher_id)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

    # Code to Commit changes and close connection : ©Prakhar Doneria 2024
    db_connection.commit()
    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()
