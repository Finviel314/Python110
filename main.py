# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Main
# # Description: Main body of applications for reading and writing employee ratings to JSON
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 11/29/2024, Initial Release
# Notes:
#  * Add this starting data to the EmployeeRatings.json file as needed.
# [{'FirstName': 'Vic', 'LastName': 'Vu', 'ReviewDate': ''1900-01-01', 'ReviewRating': 3
# ------------------------------------------------------------------------------------------------- #

from processing_classes import Employee, FileProcessor
from presentation_classes import IO

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Enter new employee rating data.
    2. Show current employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''

# Beginning of the main body of this script
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)  # Note this is the class name

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1": # Get new data (and display the change)
        #TODO Code is not looping when non alpha names are entered.
        while True:
            try:
                employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name
                IO.output_employee_data(employee_data=employees)
            except Exception as e:
                IO.output_error_messages(e)
            break

    elif menu_choice == "2":   # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop