import os.path
from helper_functions import *

# Check if student and course records exist
students_file_exists = os.path.exists("students_records.txt")
courses_file_exists = os.path.exists("courses_records.txt")

# If they don't create a new file for them
if students_file_exists == False:
    students_file = open("students_records.txt", "x")

if courses_file_exists == False:
    courses_file = open("courses_records.txt", "x")

# Create main function to manage student enrollments


def manage_student_enrollment():
    while True:
        display_welcome_menu()
        # Get user choice
        user_choice = input('Enter a number from above: ')

        # Validate user's input before proceeding
        check_result = validate_user_choice(user_choice, 'welcome_menu')
        if check_result == -1:
            print('Enter a valid option!')

        # Perform user choice based on number
        elif check_result == True:
            perform_user_choice(user_choice)


# Call on main function
manage_student_enrollment()
