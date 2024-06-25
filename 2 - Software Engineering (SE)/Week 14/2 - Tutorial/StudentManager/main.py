from datetime import date
from student_manager import StudentManager
from utils import draw_line


MAIN_MENU = """Student Manager

1. View Students
2. Update Student
3. Add Student

0. Quit"""

STUDENT_EDIT_MENU = """Please select an option below:

1. Add Grade
2. Change Email
3. Change Phone Number

0. Back"""


def main():
    """Main program loop ."""
    student_manager = StudentManager()

    while True:
        draw_line()
        print(MAIN_MENU)
        draw_line()
        user_option = input(": ")

        if user_option == "0":
            break
        # View Students
        if user_option == "1":
            draw_line()
            print("Students:")
            draw_line()
            student_manager.view_all_students()
        # Update Student
        elif user_option == "2":
            student_id = input("Please enter the ID of the student you would like to edit:\n")
            while True:
                student = student_manager.get_student(int(student_id))
                draw_line()
                print(student)
                draw_line()
                print(STUDENT_EDIT_MENU)
                edit_option = input(": ")
                if edit_option == "0":
                    break
                if edit_option == "1":
                    subject = input("Please enter a subject: ")
                    grade = int(input("Please enter the grade score: "))
                    student_manager.add_grade(student_id, subject, grade)
                elif edit_option == "2":
                    new_email = input("Please enter new email address: ")
                    student_manager.update_student_email(student_id, new_email)
        # Add student
        elif user_option == "3":
            print("Please enter the following data to add a student:")
            name = input("Name: ")
            surname = input("Surname: ")
            date_of_birth = input("Date of Birth(DD-MM-YYYY): ")
            day, month, year = date_of_birth.split('-')
            date_of_birth = date(int(year), int(month), int(day))
            email = input("Email: ")
            phone_number = input("Phone Number: ")
            student_manager.add_student(name, surname, date_of_birth, email, phone_number)


if __name__ == "__main__":
    main()
