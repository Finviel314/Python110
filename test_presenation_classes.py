# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Testing Presentation Class
# # Description: Unittests for the presentation class application
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 12/08/2024, Initial Release
# ------------------------------------------------------------------------------------------------- #

import builtins
import unittest
from unittest.mock import patch
from data_classes import Employee
from presentation_classes import IO

class TestIO(unittest.TestCase):
    """
    Tests the IO class.
    """
    def setUp(self):
        """
        Sets up the test environment by initializing an empty employee data list and an Employee type.
        """
        self.employee_data = []
        self.employee_type = Employee

    # Test input_menu_choices
    def test_input_menu_choice(self):
        """
        Tests the `input_menu_choice` method with valid input.
        """
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')
            # self.assertRaises(ValueError)

    def test_menu_choice_invalid(self):
        """
        Tests the `input_menu_choice` method with invalid input.
        """
        with patch('builtins.input', return_value='5'):
            choice = IO.input_menu_choice()
            self.assertRaises(ValueError)

# test input_employee_data
    def test_input_employee_data(self):
        """
        Tests the `input_employee_data` method with valid input.
        """
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['John', 'Wick', '11111111', 5]):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'John')
            self.assertEqual(self.employee_data[0].last_name, 'Wick')
            self.assertEqual(self.employee_data[0].review_date, '11111111')
            self.assertEqual(self.employee_data[0].review_rating, 5)

if __name__ == '__main__':
    unittest.main()