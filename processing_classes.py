# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Processing Classes
# # Description: A collection of classes that read and write data to JSON
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 12/08/2024, Initial Release
# ------------------------------------------------------------------------------------------------- #

import json
from data_classes import Employee

class FileProcessor:
    """
    A collection of utility functions for reading and writing employee data to JSON files.

    Attributes:
        None

    Methods:
        read_employee_data_from_file(file_name, employee_data, employee_type):
            Reads employee data from a JSON file and populates the `employee_data` list.
        write_employee_data_to_file(file_name, employee_data):
            Writes employee data from the `employee_data` list to a JSON file.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        """
        Reads employee data from a JSON file and populates the `employee_data` list.

        Args:
            file_name (str): The name of the JSON file to read from.
            employee_data (list): A list to store the read employee data.
            employee_type (Employee): The class type for creating employee objects.

        Returns:
            list: The updated `employee_data` list.

        Raises:
            FileNotFoundError: If the specified file is not found.
            Exception: For any other unexpected errors.
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name=employee["FirstName"]
                    employee_object.last_name=employee["LastName"]
                    employee_object.review_date=employee["ReviewDate"]
                    employee_object.review_rating=employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Writes employee data from the `employee_data` list to a JSON file.

        Args:
            file_name (str): The name of the JSON file to write to.
            employee_data (list): A list of `Employee` objects to write to the file.

        Raises:
            TypeError: If the data in the `employee_data` list is not in the correct format.
            PermissionError: If permission is denied to write to the file.
            Exception: For any other unexpected errors.
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=4)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")
