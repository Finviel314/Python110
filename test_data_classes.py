# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Testing Data Classes
# # Description: Unittests for the data class application
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 12/08/2024, Initial Release
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):
    """
    Tests the `Person` class.
    """
    def test_person_init(self):
        """
        Tests the `Person` constructor with valid names.
        """
        person = Person("Bruce", "Wayne")
        self.assertEqual(person.first_name, "Bruce")
        self.assertEqual(person.last_name, "Wayne")

    def test_person_invalid_name(self):
        """
        Tests the `Person` constructor with invalid names.
        """
        with self.assertRaises(ValueError):
            person = Person("123", "Wayne")
        with self.assertRaises(ValueError):
            person = Person("Bruce", "123")

class TestEmployee(unittest.TestCase):
    """
    Tests the `Employee` class.
    """
    def test_employee_init(self):  # Tests the constructor
        """
        Tests the `Employee` constructor with valid data.
        """
        employee = Employee("Adam", "West", "19660730", 5)
        self.assertEqual(employee.first_name, "Adam")
        self.assertEqual(employee.last_name, "West")
        self.assertEqual(employee.review_date, "19660730")
        self.assertEqual(employee.review_rating, 5)

    def test_review_rating_type(self):  # Test the gpa validation
        """
         Tests the `Employee` constructor with an invalid review rating.
         """
        with self.assertRaises(ValueError):
            employee = Employee("Val", "Kilmer", "invalid_gpa")

if __name__ == '__main__':
    unittest.main()