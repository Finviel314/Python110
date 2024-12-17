# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Presentation Classes
# # Description: A collection of classes that present data to the console
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 12/08/2024, Initial Release
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee

class IO:
    """
    A collection of input/output functions for user interaction and data display.

    Methods:
        output_error_messages(message, error):
            Displays an error message to the user, optionally including a technical error message.
        output_menu(menu):
            Displays a menu of options to the user.
        input_menu_choice():
            Prompts the user to enter a menu choice and validates the input.
        output_employee_data(employee_data):
            Displays a formatted list of employee data.
        input_employee_data(employee_data, employee_type):
            Prompts the user for employee information and adds it to the `employee_data` list.
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays an error message to the user, optionally including a technical error message.

        Args:
            message (str): The user-friendly error message to display.
            error (Exception, optional): The technical error object, if available.

        Returns:
            None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """
        Displays a menu of options to the user.

        Args:
            menu (str): The menu text to be displayed.

        Returns:
            None
        """
        print()
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to enter a menu choice and validates the input.

        Returns:
            str: The user's valid menu choice.

        Raises:
            Exception: If the user enters an invalid choice.
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice


    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Displays a formatted list of employee data.

        Args:
            employee_data (list): A list of `Employee` objects to be displayed.

        Returns:
            None
        """
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations"

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """
        Prompts the user for employee information and adds it to the provided list.

        Args:
            employee_data (list): A list of `Employee` objects to append to.
            employee_type (Employee): The type of `Employee` object to create.

        Returns:
            list: The updated list of `Employee` objects.

        Raises:
            ValueError: If the user enters invalid input (e.g., non-integer review rating).
            Exception: For any other unexpected errors.
        """
        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return employee_data

        # try:
        #     employee = Employee()
        #     while True:  # Will check if alpha for name and loop until valid entry
        #         try:
        #             employee.first_name = input('Enter the employees first name: ')
        #             if not employee.first_name.isalpha():
        #                 raise ValueError('Name cannot contain numbers or special characters.')
        #             break
        #         except ValueError as e:
        #             print(e)
        #     while True:  # Will check if alpha for name and loop until valid entry
        #         try:
        #             employee.last_name = input('Enter the students last name: ')
        #             if not employee.last_name.isalpha():
        #                 raise ValueError('Name cannot contain numbers or special characters.')
        #             break
        #         except ValueError as e:
        #             print(e)
        #     employee.review_date = input("What is their review date? ")
        #     employee.review_rating = input("What is their review rating? ")
        #     employee_data.append(employee)
        # except Exception as e:
        #     IO.output_error_messages("There was a non-specific error!", e)
        # return employee_data
