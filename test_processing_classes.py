# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Testing Processing Class
# # Description: Unittests for the processing class application
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 12/08/2024, Initial Release
# ------------------------------------------------------------------------------------------------- #

import unittest
import tempfile
import json

import data_classes
from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    """
    Tests the `FileProcessor` class.
    """
    def setUp(self):
        """
        Creates a temporary file for testing and initializes empty employee data and employee type.
        """
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []
        self.employee_type = Employee

    def tearDown(self):
        """
        Closes and deletes the temporary file after each test.
        """
        self.temp_file.close()

# Test read_employee_data_from_file

    def test_read_data_from_file(self):
        """
        Tests reading employee data from a JSON file.

        - Creates sample employee data and writes it to a temporary file.
        - Calls `read_employee_data_from_file` and verifies the returned data.
        """
        sample_data = [
            {"FirstName": "John", "LastName": "Wick", "ReviewDate": '11111111', "ReviewRating": 5},
            {"FirstName": "Adam", "LastName": "West", "ReviewDate": '19660730', "ReviewRating": 5},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, Employee)

    #     # Assert that the student_data list contains the expected student objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, 'John')
        self.assertEqual(self.employee_data[0].last_name, 'Wick')
        self.assertEqual(self.employee_data[0].review_date, '11111111')
        self.assertEqual(self.employee_data[0].review_rating, 5)

# Test write_employee_data_from_file

    def test_write_data_to_file(self):
        """
        Tests writing employee data to a JSON file.

        - Creates sample employee objects.
        - Calls `write_employee_data_to_file` to write them to the temporary file.
        - Reads the written data and verifies its content.
        """
        sample_employees = [
            data_classes.Employee("John", "Doe", '19871218', 5),
            data_classes.Employee("Alice", "Smith", '19881103', 3),]

    # Call the write_employee_data_to_file method and write our temp data to it.
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        with open(self.temp_file_name, 'r') as file:
                file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]['FirstName'], 'John')
        self.assertEqual(file_data[1]['ReviewRating'], 3)

if __name__ == '__main__':
    unittest.main()