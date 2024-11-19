# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates building classes and functions to handle operations within out programs
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 11/16/2024, Initial Release
# Notes:
#  * Add this starting data to the Enrollments.json file as needed.
# [{'FirstName': 'Vic', 'LastName': 'Vu', 'CourseName' : 'Python 100'
# ------------------------------------------------------------------------------------------ #

import json

# Global Variables
FILE_NAME: str = 'Enrollments.json' # File name for storing student data
MENU = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''

#Main Data Structure
students: list = []  # A list to store student information
menu_choice: str  # Holds the choice made by the user.

# File Processing Class
class FileProcessor:
    """
    Handles file operations for reading and writing student data to a JSON file.

    Provides methods to:
    - Read student data from a specified JSON file.
    - Write student data to a specified JSON file.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data=None):
        """Reads student data from a JSON file.

        Args:
            file_name: The name of the JSON file.
            student_data: An optional list of student dictionaries. If provided,
                it will be used as the default data if the file is not found.

        Returns:
            A list of student dictionaries, either read from the file or the provided
            default data.
        """
        if student_data is None:
            student_data = students
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages('File does not exist, please create a file called Enrollments.json.', e)
        except Exception as e:
            IO.output_error_messages('There was an non specific error.', e)

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes student data to a JSON file.

        Args:
            file_name: The name of the JSON file.
            student_data: A list of student dictionaries.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(student_data, file, indent=4)
            print('The following data was saved to file.')
            for student in student_data:
                print(f'Student {student['FirstName']} '
                      f'{student['LastName']} is enrolled in {student['CourseName']}')
        # Move error handling to IO
        except FileNotFoundError as e:
            IO.output_error_messages('File does not exist, please create a file called Enrollments.json.', e)
        except Exception as e:
            IO.output_error_messages('There was an non specific error.', e)
        finally:
            if not file.closed:
                file.close()
# End of Class Definition

# Input/Output Class
class IO:
    """
    A class for input/output operations in the course registration program.
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Prints an error message to the console.

        Args:
            message: The error message to display.
            error: An optional exception object to provide more detailed information.
        """
        print(message, end='\n\n')
        if error is not None:
                print('-- Technical Error Message -- ')
                print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_student_courses(student_data: list):
        """Prints a formatted list of students and their courses.

        Args:
            student_data: A list of student dictionaries.
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student['FirstName']} '
                  f'{student['LastName']} is enrolled in {student['CourseName']}')
        print('-' * 50)

    @staticmethod
    def output_menu():
        """Prints the main menu to the console."""
        print(MENU)

    @staticmethod
    def input_menu_choice():
        """Prompts the user to enter a menu choice and validates the input.

        Returns:
            The user's selected menu choice as a string.
        """
        # Define function block
        choice = '0'
        try:
            choice = input('Enter your menu choice number: ')
            if choice not in ('1', '2', '3', '4'):
                raise Exception('You must choose 1, 2, 3, or 4')
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """Prompts the user to enter student information and adds it to the list.

        Args:
            student_data: A list of student dictionaries.
        """
        try:
            while True:
                try:
                    student_first_name = input('Enter the students first name: ')
                    if not student_first_name.isalpha():
                        raise ValueError('Name cannot contain numbers.')
                    break
                except ValueError as e:
                    print(e)
            while True:
                try:
                    student_last_name = input('Enter the students last name: ')
                    if not student_last_name.isalpha():
                        raise ValueError('Name cannot contain numbers.')
                    break
                except ValueError as e:
                    print(e)
            course_name = input('Enter the course name: ')
            student_data.append({'FirstName': student_first_name,
                             'LastName': student_last_name,
                             'CourseName': course_name})
        except Exception as e:
            IO.output_error_messages('There was a non-specific error when adding data.', e)

#End of class definition

# Main Body of Script
students = FileProcessor.read_data_from_file(FILE_NAME, student_data=students)

while True:
    IO.output_menu()
    menu_choice = IO.input_menu_choice()

    if menu_choice == '1':
        IO.input_student_data(student_data=students)
        print('\nHere is the current data:')
        IO.output_student_courses(student_data=students)

    elif menu_choice == '2':
        IO.output_student_courses(student_data=students)

    elif menu_choice == '3':
        FileProcessor.write_data_to_file(FILE_NAME, student_data=students)

    elif menu_choice == '4':
        print('Goodbye!')
        break  # out of the while loop