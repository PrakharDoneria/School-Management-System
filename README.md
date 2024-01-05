# School-Management-System
Database Setup:The system uses a MySQL database to store information about teachers, attendance, timetable, etc.Database credentials are configured in the `config.py` file.

Teacher Management (teacher.py):
The teacher.py script provides functions to add new teachers and remove teachers from the staff.

Timetable Management (timetable.py):
The timetable.py script allows you to add or update the timetable, specifying which teacher is in charge and who the substitute is.

Attendance (attendance.py):
The attendance.py script handles marking attendance for teachers. You can mark them as absent or present.

Half Day (half_day.py):
The half_day.py script handles marking half-days for teachers.

Percentage (percentage.py):
The percentage.py script calculates the percentage of days a teacher was present based on the input Teacher ID.

Salary Calculation (salary.py):
The salary.py script calculates the total salary for a teacher, considering deductions for absent days and half-days.

View and Modify Teacher Information (view_teacher.py and modify_teacher.py):
The view_teacher.py script displays detailed information about a teacher based on the provided Teacher ID.The modify_teacher.py script allows you to update information about a teacher.

Backup Data (backup_data.py):
The backup_data.py script creates a backup of teacher data in JSON format.

Main Program (main.py):
The main.py script acts as the entry point, integrating all functionalities.Users interact with the system through a menu-driven interface.

Getting Started (requirements.txt):
Required dependencies are listed in the requirements.txt file.

Run the System:
Users can install dependencies, set up the database, and execute main.py to use the school management system.This system allows for basic management of teachers, attendance, and related information within a school. Users can perform various operations through a menu-driven interface in the command line.
