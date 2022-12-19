import sys
import student_functions
import enrollment_functions
import courses_functions
import json


def display_welcome_menu():
    '''Show available options to user on first load'''
    print('''
    WELCOME TO OVTraining Academy. What would you like to do today?
    1. Manage student records
    2. Courses
    3. Enroll student
    4. Exit
    ''')


def validate_user_choice(user_input, section):
    '''Check if user input is valid according to the section'''
    # Store menu options as strings since default input type is string
    # and for easy and effective validation
    WELCOME_MENU_OPTIONS = ['1', '2', '3', '4']
    MANAGE_STUDENT_MENU_OPTIONS = ['1', '2', '3', '4', '5']
    MANAGE_COURSES_MENU = ['1', '2', '3']

    # Validate user input
    if section == 'welcome_menu':
        if user_input in WELCOME_MENU_OPTIONS:
            return True
        else:
            return -1
    elif section == 'manage_student_menu':
        if user_input in MANAGE_STUDENT_MENU_OPTIONS:
            return True
        else:
            return -1
    elif section == 'manage_courses_menu':
        if user_input in MANAGE_COURSES_MENU:
            return True
        else:
            return -1


def check_if_decimal(item) -> str:
    '''Check if a string is decimal and then if int(str) is positive'''
    if item.isdecimal():
        if int(item) >= 0:
            return True
    else:
        return False


def student_exists(student_id, students_file_name):
    '''Checks if a student exists in students records file using an ID'''
    with open(f"{students_file_name}", "r", encoding="utf-8") as file:
        for line in file:
            # Convert line from str to python dictionary
            student = eval(line)
            if student["student_id"] == student_id:
                return True
        return -1


def course_exists(course_id, courses_file_name):
    '''Checks if a course exists in courses records file using an ID'''
    with open(f"{courses_file_name}", "r", encoding="utf-8") as file:
        for line in file:
            # Convert line from str to python dictionary
            course = json.loads(line)
            if course["course_id"] == course_id:
                return True
        return -1


def perform_user_choice(user_choice) -> str:
    '''Performs operation based on user input'''
    if user_choice == '1':
        # Manage student records
        student_functions.manage_student_records()
    elif user_choice == '2':
        # Courses
        courses_functions.manage_courses()
    elif user_choice == '3':
        # Enroll student
        student_id = input(
            "Enter student id who you want to enroll a course: ")
        course_id = input("Enter course id: ")
        enrollment_functions.enroll_student(
            student_id, course_id, "students_records.txt", "courses_records.txt")
    elif user_choice == '4':
        # Exit the program
        print('Bye for now!')
        sys.exit()
