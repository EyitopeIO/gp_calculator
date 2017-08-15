"""Module 1 is the basic property of the objects created in this program"""
import sys
import time
unit = {"A":5, "B":4, "C":3, "D":2,"F":0}



def wait(delay):
    time.sleep(delay)

def add_space(spacing):
    for i in range(0, spacing):
        print("")

def handle_special_input(special_input):
    """Always use this function at every input statement"""
    if special_input == "exit":
        sys.exit()
    elif special_input == "change":
        pass #The code to change course data should run here.
    return special_input






class Main:

    def __init__(self, no_of_courses , course_name_and_score, spacing, total_no_of_units_offered):
        self.no_of_courses = no_of_courses # integer: used as a multiplier and later on for limit of summation
        self.total_string_formatters = ['%s'] * no_of_courses #string formatting applied to this during print of table
        self.course_data ={}
        self.course_data = self.get_course_names_and_score(self.no_of_courses)
        self.total_no_of_units = total_no_of_units_offered
        self.gp = self.calculate_gp()


    def display(self, spacing): # This is upposed to show the courses and the scores underneath like a table
        for i in self.course_data:
            print(i, spacing, end="") # Print the table head
            print(self.course_data.get(i)) # Print the value corresponding to the table head.
        print("Your gp is", self.gp)


    def calculate_gp(self):

        """numerator is sum of unit * grade of course. Denominator is sum of all units."""

        courses_and_unit = {} # I'd keep course name as keys, and unit of each course here.
        # course_and_unit must first contain values before being used. First in this function

        courses_as_list = list(self.course_data)  # A list having all courses as its items

        add_space(1)
        wait(3)

        for i in range(0,self.no_of_courses): # This loop is for user to specify the unit of each course.

            print("How many units is course ", courses_as_list[i], "?")
            entered_unit = ""

            while True:
                try:
                    entered_unit = int(handle_special_input(input()))
                except ValueError:
                    print("Invalid input.")
                break # Continue if all's well with the input

            courses_and_unit.setdefault(courses_as_list[i], entered_unit)
        # At this point, course_and_unit contains the unit of each course

        numerator = 0 # Used in the loop below
        for i in range(0, self.no_of_courses-1):

            numerator = numerator + float((courses_and_unit.get(courses_as_list[i]) * self.change_to_unit(
                self.course_data.get(courses_as_list[i]))))

        gp = numerator / self.total_no_of_units
        round(gp,2) # Round to 2 decimal places
        return gp


    def get_course_names_and_score(self, no_of_courses):

        """This just gets a dictionary consisting of course name and score ready"""

        print("Program will now collect your course name and score.\n")
        wait(2)

        for i in range(1, no_of_courses + 1):
            add_space(1)  # It justs adds a blank line.
            print("course", i)
            course_name = handle_special_input(input("Enter course name: ").upper())  # I want everything printed in upper case
            course_score = handle_special_input(input("Enter course score/grade: "))
            self.course_data.setdefault(course_name, course_score)

        return self.course_data


    def change_to_unit(self, to_be_converted):

        """This function converts grade or score to unit.
        Paremeter to_be_converted is a string"""

        grade = 0
        if str(to_be_converted).isdigit():# if to_be_converted is a number

            to_be_converted = int(to_be_converted)
            if to_be_converted in range(0, 44 + 1):  # 0-44
                grade = unit.get("F")
            elif to_be_converted in range(45, 50):  # 45-49
                grade = unit.get("D")
            elif to_be_converted in range(50, 60):  # 50-59
                grade = unit.get("C")
            elif to_be_converted in range(60, 70):  # 60-69
                grade = unit.get("B")
            elif to_be_converted in range(70, 101):  # 70-100
                grade = unit.get("A")

        elif str(to_be_converted).isalpha():
            if to_be_converted.upper() in unit:
                grade = unit.get(to_be_converted.upper())

        return grade  # At this point, this should be a number.
