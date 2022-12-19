# Import necessary modules
import helper_functions
import json


def display_courses_menu():
    '''Show available options to user for managing courses'''
    print('''
    COURSES
    1. Display all courses
    2. Add a new course
    3. Return to main menu
    ''')


def display_all_courses(courses_file_name) -> str:
    '''Prints all courses from course txt file'''
    print('ALL AVAILABLE COURSES')
    # Put code in try except block to avoid crashing(in case file does not exist)
    try:
        with open(f"{courses_file_name}", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    except:
        print('Ensure the course records file exists!')


def add_new_course(course_id, course_name, course_hours, course_file_name):
    '''Adds a new course to course records'''
    # Create structure
    new_course = {
        "course_id": course_id,
        "course_name": course_name,
        "course_hours": course_hours
    }

    # Convert new course from dictionary to string
    new_course_str = json.dumps(new_course)

    # Open the file in append and read mode ('a+')
    with open(f"{course_file_name}", "a+") as file:
        # Move read cursor to the start of file.
        file.seek(0)
        # If file is not empty then add new line('\n')
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")
        # Add course at the end of file
        file.write(new_course_str)


def manage_courses():
    '''Manages courses'''
    while True:
        '''Displays course information and gives access to add courses'''
        display_courses_menu()
        user_choice = input(
            'Enter a number from above to manage courses records: ')

        check_user_choice_result = helper_functions.validate_user_choice(
            user_choice, 'manage_courses_menu')
        # If user choice is valid call on corresponding functions
        if check_user_choice_result == True:
            if user_choice == '1':
                # Display all courses and their records
                display_all_courses("courses_records.txt")

            elif user_choice == '2':
                # Add a new course
                course_id = input('Enter course ID: ')
                course_name = input('Enter course name: ')
                course_hours = input('Enter the number of course hours: ')

                # Check if course exists
                course_exists_result = helper_functions.course_exists(
                    course_id, "courses_records.txt")
                if course_exists_result == True:
                    print('Course already exists!')
                    return -1

                # Check that both course id and course hours are positive and valid
                course_id_check = helper_functions.check_if_decimal(course_id)
                course_hours_check = helper_functions.check_if_decimal(
                    course_hours)
                if (course_id_check and course_hours_check) == True:
                    add_new_course(
                        course_id, course_name, course_hours, "courses_records.txt")
                    print(f'{course_name} added successfully')
                else:
                    print('Ensure all details are entered correctly!')

            elif user_choice == '3':
                # Break inner loop and return to main menu
                break
        else:
            print('Enter a valid option!')
