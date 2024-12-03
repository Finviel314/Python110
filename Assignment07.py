# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment further refactors are code by creating Person and Student Classes
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 11/29/2024, Initial Release
# Notes:
#  * Add this starting data to the Enrollments.json file as needed.
# [{'FirstName': 'Vic', 'LastName': 'Vu', 'CourseName' : 'Python 100'
# ------------------------------------------------------------------------------------------ #

import json

# Constant Variables
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
students: list = []  # Stores student information
menu_choice: str  # Holds the choice made by the user.
class Person:
    def __init__(self, first_name: str = '', last_name: str = ''):
        """
        Initializes a Person object.

        Args:
            first_name (str, optional): The person's first name. Defaults to an empty string.
            last_name (str, optional): The person's last name. Defaults to an empty string.
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Gets the person's first name.

        Returns:
            str: The person's first name, capitalized.
        """
        return self._first_name.title()  # Capitalizes first letter of name

    @first_name.setter
    def first_name(self, value: str):
        """
        Sets the person's first name.

        Args:
            value (str): The new first name.

        Raises:
            ValueError: If the new first name contains non-alphabetic characters.
        """
        if value.isalpha() or value == '':  # checks if alpha or number
            self._first_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    @property
    def last_name(self):
        """
        Gets the person's last name.

        Returns:
            str: The person's last name, capitalized.
        """
        return self._last_name.title()  # Capitalizes first letter of name

    @last_name.setter
    def last_name(self, value: str):
        """
        Sets the person's last name.

        Args:
            value (str): The new last name.

        Raises:
            ValueError: If the new last name contains non-alphabetic characters.
        """
        if value.isalpha() or value == '':  # checks if alpha or number
            self._last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

class Student(Person):
    def __init__(self, first_name: str = '', last_name: str = '', course: str = ''):
        """
        Initializes a Student object.

        Args:
            first_name (str, optional): The student's first name. Defaults to an empty string.
            last_name (str, optional): The student's last name. Defaults to an empty string.
            course (str, optional): The student's course. Defaults to an empty string.
        """
        self._course = course
        super().__init__(first_name=first_name, last_name=last_name)
    @property
    def course(self):
        """
        Gets the student's course.

        Returns:
            str: The student's course.
        """
        return self._course

    @course.setter
    def course(self, value: str):
        """
        Sets the student's course.

        Args:
            value (str): The new course.
        """
        self._course = value

    def __str__(self):
        return f'first_name: {self.first_name}, last_name: {self.last_name}, course: {self.course}'

# File Processing Class
class FileProcessor:
    """
    Handles file operations for reading and writing student data to a JSON file.

    Provides methods to:
    - Read student data from a specified JSON file.
    - Write student data to a specified JSON file.
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data):
        """
        Reads student data from a JSON file.

        Args:
            file_name (str): The name of the JSON file.
            student_data (list): A list of Student objects to populate.

        Returns:
            list: The updated list of Student objects.
        """
        try:
            with open(file_name, 'r') as file:
                list_of_dict = json.load(file)
                for student in list_of_dict:
                    student_object: Student = Student(first_name=student["FirstName"],
                                            last_name=student['LastName'],
                                            course=student['CourseName'])
                    student_data.append(student_object)
        except FileNotFoundError as e:
            IO.output_error_messages('File does not exist, please create a file called Enrollments.json.', e)
        except Exception as e:
            IO.output_error_messages('There was an non specific error.', e)
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes student data to a JSON file.

        Args:
            file_name (str): The name of the JSON file.
            student_data (list): A list of Student objects to write.
        """
        try:
            list_of_dict: list = []
            for student in student_data:
                student_json: dict = {'FirstName': student.first_name,
                                      'LastName': student.last_name,
                                      'CourseName': student.course}
                list_of_dict.append(student_json)

            file = open(file_name, 'w')
            json.dump(list_of_dict, file, indent=4)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages('File does not exist, please create a file called Enrollments.json.', e)
        except Exception as e:
            IO.output_error_messages('There was an non specific error.', e)

# End of Class Definition

# Input/Output Class
class IO:
    """
    A class for input/output operations in the course registration program.
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Prints an error message to the console.

        Args:
            message (str): The error message to display.
            error (Exception, optional): The exception object, if any.
        """
        print(message, end='\n\n')
        if error is not None:
                print('-- Technical Error Message -- ')
                print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Prints a formatted list of students and their courses.

        Args:
            student_data (list): A list of Student objects.
        """
        print("-" * 50)
        for student in student_data:
            print(student.first_name, student.last_name, student.course)
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
        """
        Prompts the user to enter student information and adds it to the list.

        Args:
            student_data (list): A list of Student objects.
        """
        try:
            student = Student()
            while True: # Will check if alpha for name and loop until valid entry
                try:
                    student.first_name = input('Enter the students first name: ')
                    if not student.first_name.isalpha():
                        raise ValueError('Name cannot contain numbers or special characters.')
                    break
                except ValueError as e:
                    print(e)
            while True:  # Will check if alpha for name and loop until valid entry
                try:
                    student.last_name = input('Enter the students last name: ')
                    if not student.last_name.isalpha():
                        raise ValueError('Name cannot contain numbers or special characters.')
                    break
                except ValueError as e:
                    print(e)

            student.course = input('Enter the students course: ')
            student_data.append(student)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
# Code for that does not loop and ask for continued input until correct format (can delete later)
        # try:
        #     # Input Data
        #         student= Student()
        #         student.first_name = input('Enter the students first name: ')
        #         student.last_name = input('Enter the students last name: ')
        #         student.course = input('Enter the students course: ')
        #         student_data.append(student)
        # except ValueError as e:
        #     IO.output_error_messages("That value is not the correct type of data!", e)
        # except Exception as e:
        #     IO.output_error_messages("There was a non-specific error!", e)
        # return student_data

# Start of Main

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

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
        print('The following data was saved to file: ')
        IO.output_student_courses(student_data=students)

    elif menu_choice == '4':
        print('Goodbye!')
        break  # out of the while loop