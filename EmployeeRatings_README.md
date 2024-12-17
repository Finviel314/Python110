# Employee Rating Application

This Python application provides a user-friendly interface to manage employee ratings. It allows users to:

- Enter new employee ratings by adding new employees with their names, review dates, and ratings.
- View current employee ratings and display a list of all employees with their details.
- Persist the employee data to a JSON file for future reference.
- Exit the program: Terminate the application.

---
## Repository  
[GitHub Repository] - https://github.com/Finviel314/Python110

---
## Class Documentation

### `Person` Class

This class represents an individual with attributes for the first name and last name.

#### Attributes

- `first_name` (str): The first name of the person.
- `last_name` (str): The last name of the person.

#### Methods

##### `__init__(self, first_name: str = "", last_name: str = "")`

- Initializes a new `Person` object.
- Parameters:
  - `first_name` (str, optional): The first name of the person. Defaults to an empty string.
  - `last_name` (str, optional): The last name of the person. Defaults to an empty string.

##### `__str__(self) -> str`

- Returns a formatted string representation of the `Person` object in the following format: "First Name,Last Name."

##### Property Methods

###### `first_name (property)`
- Retrieves the first name of the person with the first letter capitalized.

###### `first_name (setter)`
- Sets the first name of the person, ensuring it contains only alphabetic characters or is an empty string.

###### `last_name (property)`
- Retrieves the last name of the person with the first letter capitalized.

###### `last_name (setter)`
- Sets the last name of the person, ensuring it contains only alphabetic characters or is an empty string.
---
### `Employee` Class (Inherits from `Person`)

The `Employee` class is a subclass of `Person` and represents an employee with additional attributes for review date and review rating.

#### Attributes

- `first_name` (str): The first name of the employee (inherited from `Person`).
- `last_name` (str): The last name of the employee (inherited from `Person`).
- `review_date` (str): The employee's review date in the format "YYYY-MM-DD."
- `review_rating` (int): The employee's review rating (1-5).

#### Methods

##### `__init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3)`

- Initializes a new `Employee` object.
- Parameters:
  - `first_name` (str, optional): The first name of the employee. Defaults to an empty string.
  - `last_name` (str, optional): The last name of the employee. Defaults to an empty string.
  - `review_date` (str, optional): The review date of the employee. Defaults to "1900-01-01."
  - `review_rating` (int, optional): The review rating of the employee (1-5). Defaults to 3.

##### `__str__(self) -> str`

- Returns a formatted string representation of the `Employee` object in the following format: "First Name,Last Name,Review Date,Review Rating."

##### Property Methods

###### `review_date (property)`
- Retrieves the review date of the employee.

###### `review_date (setter)`
- Sets the review date of the employee, ensuring it follows the "YYYY-MM-DD" format.

###### `review_rating (property)`
- Retrieves the review rating of the employee.

###### `review_rating (setter)`
- Sets the review rating of the employee, ensuring it is an integer between 1 and 5.

## Example Usage

```python
# Create an Employee object
employee = Employee("John", "Doe", "2024-12-01", 5)
print(employee)  # Output: "John,Doe,2024-12-01,5"
 ```
---
### `FileProcessor` Class

This class provides methods for reading and writing employee data to JSON files.

#### Methods

##### `read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee)`

- Reads employee data from a JSON file and populates the `employee_data` list.
- Parameters:
  - `file_name` (str): The name of the JSON file to read from.
  - `employee_data` (list): A list to store the read employee data.
  - `employee_type` (Employee): The class type for creating employee objects.
- Returns:
  - The updated `employee_data` list.

##### `write_employee_data_to_file(file_name: str, employee_data: list)`

- Writes employee data from the `employee_data` list to a JSON file.
- Parameters:
  - `file_name` (str): The name of the JSON file to write to.
  - `employee_data` (list): A list of `Employee` objects to write to the file.

---
## Example Usage
```Python
# Reading employee data from a JSON file
employee_data = []
employee_data = FileProcessor.read_employee_data_from_file("EmployeeRatings.json", employee_data, Employee)

# Print employee data after reading from the file
for emp in employee_data:
    print(emp)
    
# Writing employee data to a JSON file
FileProcessor.write_employee_data_to_file("EmployeeRatings.json", employee_data)
print("Data has been saved to the file.")

```
---
### `IO` Class

This class provides input/output functions for user interaction and data display.

#### Methods

##### `output_error_messages(message: str, error: Exception = None)`

- Displays an error message to the user, optionally including a technical error message.

##### `output_menu(menu: str)`

- Displays a menu of options to the user.

##### `input_menu_choice()`

- Prompts the user to enter a menu choice and validates the input.

##### `output_employee_data(employee_data: list)`

- Displays a formatted list of employee data.

##### `input_employee_data(employee_data: list, employee_type: Employee)`

- Prompts the user for employee information and adds it to the provided list of employee data.

---
## Example Usage
```Python
# Display the menu
IO.output_menu(MENU)

# Getting user input for menu choice
menu_choice = IO.input_menu_choice()
print(f"User selected menu option: {menu_choice}")

# Displaying employee data
IO.output_employee_data(employee_data)

# Input new employee data
employee_data = IO.input_employee_data(employee_data, Employee)
```
---
# Main Program

## Overview
This is an Employee Rating Application designed to collect, store, and process performance ratings for employees. 
It allows users to input ratings, view employee data, and save this information to a file. 
The application helps managers assess employee performance by giving structured ratings based on predefined criteria. 
The app is built in Python and handles common functionalities like data input validation, file handling, and user interaction through a console interface.

## Features
- Allows managers to enter employee data including names, review dates, and performance ratings.
- Validates inputs to ensure correct data format and acceptable rating values.
- Displays a menu for users to select actions such as entering data, viewing data, or saving data.
- Reads and writes employee data to/from a JSON file.

## Console Interface
    1.Enter new employee rating data.
    2.Show current employee rating data.
    3.Save data to a file.
    4.Exit the program.

---
## Example Usage
```Python
# Initial data load from file
employees = FileProcessor.read_employee_data_from_file(FILE_NAME, employees, Employee)

# Present the menu and get the user's choice
while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        # Add a new employee
        employees = IO.input_employee_data(employees, Employee)
        IO.output_employee_data(employees)
    elif menu_choice == "2":
        # Show current employee data
        IO.output_employee_data(employees)
    elif menu_choice == "3":
        # Save data to file
        FileProcessor.write_employee_data_to_file(FILE_NAME, employees)
        print(f"Data saved to {FILE_NAME}")
    elif menu_choice == "4":
        # Exit the program
        break
```
