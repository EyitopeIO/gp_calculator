import Module1



"""
*** PROGRAMMER'S NOTE ***
----------------------------------------------------------------------------
Written by Eyitope Adelowo in just about a week.

This progrm was written to be used during a python tutorial at school. It applies many simple Python concepts ranging
from string manipulations to data structures, modules and even classes.
---------------------------------------------------------------------------


*** NOTE TO STUDENTS ***
-------------------------------------------------------------------------------------------------------------------
I didn't check indepth for bugs, so test as much as possible. Let me know if there's a bug you can't fix. Send me the
original file with details of the bug before the first line of code. Don't remove my comments please!

Program responds to user input. If a user types 'exit' anytime as an input, program quits. It should also
respond to input like 'change score CSC202', and 'change course CSC202', but I didn't implement that since this is just
a tutorial. Try it. You may also implement this with a GUI. There wx, tkinter, Qt.

Contact me on whatsapp +2348095927348 or call on +2348142357637 if you need any help. And don't ask how I am, please.
Simply introduce yourself and get to the point.
--------------------------------------------------------------------------------------------------------------------
"""




def main_program():

    print("*** GP CALCULATOR ***\n")

    while True:
        try:
            no_of_courses = int(Module1.handle_special_input(input("Type how many courses are you offering: ")))

            total_no_of_units_offered = int(
                Module1.handle_special_input(input("How many units are you having this semester? ")))

        except ValueError:
            print("Invalid input")
        else:
            break

    gp_object = Module1.Main(no_of_courses=no_of_courses, course_name_and_score=None, spacing="  ",
                             total_no_of_units_offered=total_no_of_units_offered)

    gp_object.display("   ")
    print("\n END OF PROGRAM")
    input()


if __name__ == "__main__": # Run if you're the first module, and not being called by another.
    main_program()


