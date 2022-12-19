import helper_functions
import courses_functions
import json


def check_if_enrolled(student_courses, course_to_enroll):
    '''Checks if a student is enrolled in a course'''
    for course in student_courses:
        if course == course_to_enroll:
            return True
    return False


def get_student(student_id, students_file_name):
    '''Returns a particular student details using a student ID'''
    with open(f"{students_file_name}", "r", encoding="utf-8") as file:
        for line in file:
            # Convert line from str to python dictionary
            student = eval(line)
            if student["student_id"] == student_id:
                return student
        return 'Student not found'


def get_course_name(course_id, courses_file_name):
    '''Returns a particular course details using a course ID'''
    with open(f"{courses_file_name}", "r", encoding="utf-8") as file:
        for line in file:
            # Convert line from str to python dictionary
            course = json.loads(line)
            if course["course_id"] == course_id:
                return course["course_name"]
        return 'Course not found'


def enroll_student(student_id, course_id, students_file_name, courses_file_name):
    '''Enrolls students'''
    # Put code in try except block to avoid crash of program
    try:
        # First Check if student id is in list of records
        student_exists_check = helper_functions.student_exists(
            student_id, students_file_name)

        # Check if course id is in list of records
        course_exists_check = helper_functions.course_exists(
            course_id, courses_file_name)

        # If both checks pass, get course and student
        if student_exists_check == True and course_exists_check == True:
            # Get course name
            course = get_course_name(course_id, courses_file_name)
            # Get student
            student = get_student(student_id, students_file_name)
            student_name = student["student_name"]
            # Check if student has enrolled in a particular course
            student_courses = student["courses_enrolled_in"]
            check_if_enrolled_result = check_if_enrolled(
                student_courses, course)
            if check_if_enrolled_result == True:
                print('Student has already enrolled in the course!')
                return -1
            else:
                student_courses.append(course)
                update_student_courses(
                    student_id, students_file_name, str(student))
                print(f"{student_name} has successfully enrolled in {course}")
        else:
            print('Make sure student id and course id are correct/exist!')
    except:
        print('An error occured!')


def update_student_courses(student_id, students_file_name, student):
    '''Updates a student's record using the id and updated details'''
    # Get all lines from the file
    with open(f"{students_file_name}", "r", encoding="utf-8") as file:
        # Get list of lines of the file
        lines = file.readlines()

        for line in lines:
            # Convert line from str to python dictionary
            student_dic = eval(line)
            if student_dic["student_id"] == student_id:
                # Remove student(line)
                lines.remove(line)
                # Add updated student
                lines.append(f"{student}")
                # Break loop after student courses is updated
                break
        # Open the student file and write the records
        with open(f"{students_file_name}", "w") as file:
            for line in lines:
                file.write(line)
