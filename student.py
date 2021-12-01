# ----------------------------------------------------------------
# Author: Max Clingroth
# Date: 11/17/21
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(id, c_roster):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # -------------------------------------------------------------
    # Creates a list and iterates over the dictionary, storing classes taken in the list
    coursesEnrolled = []
    courseIterable = c_roster.items()
    for course, students in courseIterable:
        if id in students:
            coursesEnrolled.append(course)
    print('Courses registered:')
    for item in coursesEnrolled:
        print(item)
    print('Total number:', len(coursesEnrolled))


def add_course(id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    course = input('Enter course you want to add: ')

    # Tests if the course entered is a key in the c_roster dictionary
    if course not in c_roster:
        print('Course not found')

    # Tests if the id is in the list associated with the course key
    elif id in c_roster[course]:
        print('You are already enrolled in that course.')

    # Tests if the length of the list for the course is equal to the max size of the course
    elif len(c_roster[course]) >= c_max_size[course]:
        print('Course already full.')

    else:
        c_roster[course].append(id)
        print('Course added')


def drop_course(id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------
    course = input('Enter course you want to drop: ')

    # Tests if the course entered is a key in the c_roster dictionary
    if course not in c_roster:
        print('Course not found')

    # Tests if the id is not in the list associated with the course key
    elif id not in c_roster[course]:
        print('You are not enrolled in that course.')

    else:
        c_roster[course].remove(id)
        print('Course dropped')