import helper_functions
import json


def display_student_record_menu():
    '''Show available options to user for managing students'''
    print('''
    MANAGE STUDENT RECORDS
    1. Display all students
    2. Add a student
    3. Remove a student
    4. Search for a student using their ID
    5. Return to main menu
    ''')


def display_all_students(students_file_name) -> str:
    '''Prints all students'''
    print('ALL STUDENTS')
    # Put code in try except block to avoid crashing(in case file does not exist or deleted unexpectedly)
    try:
        with open(f"{students_file_name}", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    except:
        print('Ensure the student records file exists!')


def add_student(student_id, student_name, students_file_name):
    '''Add a new student to student list'''
    # Create structure
    new_student = {
        "student_id": student_id,
        "student_name": student_name,
        "courses_enrolled_in": []
    }

    # Convert new student from dictionary to string
    new_student_str = json.dumps(new_student)

    # Open the file in append and read mode ('a+')
    with open(f"{students_file_name}", "a+") as file:
        # Move read cursor to the start of file.
        file.seek(0)
        # If file is not empty then add  a new line ('\n')
        data = file.read(100)
        if len(data) > 0:
            file.write("\n")
        # Add new student details to the end of file
        file.write(new_student_str)


def remove_student(student_id, students_file_name):
    '''Deletes a student's record using the id'''
    # First Check if student id is in list of records
    student_exists_check = helper_functions.student_exists(
        student_id, students_file_name)

    if student_exists_check == True:
        # Get all lines from the file
        with open(f"{students_file_name}", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                # Convert line from str to python dictionary
                student = eval(line)
                if student["student_id"] == student_id:
                    lines.remove(line)
                    print(
                        f'{student["student_name"]} record deleted successfully')

            # Add student records that were not deleted back to file
            with open(f"{students_file_name}", "w") as file:
                for line in lines:
                    file.write(line)

    else:
        print('Student record not found. Enter correct student ID!')


def search_student(student_id, students_file_name):
    '''Searches through students records file using a student ID'''
    with open(f"{students_file_name}", "r", encoding="utf-8") as file:
        for line in file:
            # Convert line from str to python dictionary
            student = eval(line)
            if student["student_id"] == student_id:
                return student
        return 'Student not found'


def manage_student_records():
    '''Manages student records'''
    while True:
        # Display available options
        display_student_record_menu()
        user_choice = input(
            'Enter a number from above to manage student records: ')

        check_result = helper_functions.validate_user_choice(
            user_choice, 'manage_student_menu')

        # If user choice is valid call on corresponding functions
        if check_result == True:
            if user_choice == '1':
                # Display all student and their records
                display_all_students("students_records.txt")

            elif user_choice == '2':
                # Add a student
                print('ADD A STUDENT')
                student_id = input('Enter the ID for your new student: ')
                student_exists_check = helper_functions.student_exists(
                    student_id, "students_records.txt")
                if student_exists_check == True:
                    print('Student already exists!')
                else:
                    # Check that the inputted value consists of decimal numbers only
                    check_user_input = helper_functions.check_if_decimal(
                        student_id)
                    if check_user_input == True:
                        student_name = input('Enter student name: ')
                        add_student(student_id, student_name,
                                    "students_records.txt")
                        print(f"New student:{student_name} added successfully")

            elif user_choice == '3':
                print('REMOVE A STUDENT')
                # Remove a student using their ID
                student_id = input('Enter a student id: ')
                remove_student(student_id, "students_records.txt")

            elif user_choice == '4':
                print("SEARCH FOR A STUDENT")
                # Search a student using their ID
                student_id = input('Enter a student id: ')
                print(search_student(student_id, "students_records.txt"))

            elif user_choice == '5':
                # Break inner loop and return to main menu
                break
        else:
            print('Enter a valid option!')
