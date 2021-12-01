# ----------------------------------------------------------------
# Author: Max Clingroth
# Date: 11/17/21
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function calculate billing information. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # This function returns the number of course hours and tuition
    # cost.
    # ------------------------------------------------------------
    # Uses an iterable to find the classes a student is enrolled in and adds them to a list
    coursesEnrolled = []
    courseIterable = c_rosters.items()
    for course, students in courseIterable:
        if id in students:
            coursesEnrolled.append(course)

    # Calculates number of hours using the value associated with each class in the list
    hours = 0
    for course in coursesEnrolled:
        hours += c_hours[course]
    if s_in_state[id]:
        return hours, (hours * 225.0)
    else:
        return hours, (hours * 850.0)


def display_hours_and_bill(hours, cost):
    # ------------------------------------------------------------
    # This function prints the number of course hours the student
    # is taking and the total tuition cost. It takes two parameters:
    # hours and cost. This function has no return value.
    # ------------------------------------------------------------
    print(f'Course load: {hours} credit hours')
    print(f'Enrollment cost: ${cost:.2f}')
