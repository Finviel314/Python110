# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment adds dictionaries and error handling
# Change Log: (Who, When, What)
#  #  Andrew Yarberry, 11/07/2024, Initial Release
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = 'Enrollments.csv'

# Define the Data Variables
menu_choice: str = ''
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: dict[str,str] = {}
students: list = []
csv_data: str = ''

try:
    with open(FILE_NAME, 'r') as file_obj:  # With open will auto close the file
        for line in file_obj.readlines():  # steps through the file and reads each line appending data to students
            student = line.strip().split(',')
            student_data = {'first_name':student[0], 'last_name':student[1],'course_name':student[2]}
            students.append(student_data)
        del students[0] #Deletes headers in file
except FileNotFoundError as e:
        print(f'Error: File "{FILE_NAME}" not found.')
except Exception as e:
    print(f'There was a non specific error')
    print('---Technical Error Message---')
    print(e, e.__doc__, type(e), sep='\n')

# Present Menu of Choices
while True:
    print(MENU)
    menu_choice = input('Please enter a selection: ')

    # Get data from the user and append it with current data in the file
    #Added error handling but does not loop back through to reenter
    if menu_choice == '1':
        try:
            student_first_name = input('Input your first name: ')
            if not student_first_name.isalpha():
                raise ValueError("There first name must be alphabetic")
        except ValueError as e:
                    print(e)
        try:
            student_last_name = input('Input your last name: ')
            if not student_first_name.isalpha():
                raise ValueError("There first name must be alphabetic")
        except ValueError as e:
                    print(e)
        course_name = input('Input course: ')
        student_data = {'first_name': student_first_name,
                            'last_name': student_last_name,
                            'course_name':course_name}
        students.append(student_data)  # This will add the user information to the list of lists

    # Print current data to screen
    elif menu_choice == '2':
        for student in students:
            print(f'{student['first_name']},'
                  f'{student['last_name']},'
                  f'{student['course_name']}')

    # Process all user data to file

    elif menu_choice == '3':
        try:
            with open(FILE_NAME, 'w') as file_obj:
                file_obj.write(f'{'first_name'},{'last_name'},{'course_name'}\n') #Creates headers in file
                for student in students:
                    file_obj.write(f'{student['first_name']},'
                                   f'{student['last_name']},'
                                   f'{student['course_name']}\n')
            print(f'The following students have been added to file:')
            for student in students:
                print(f'{student['first_name']},'
                      f'{student['last_name']},'
                      f'{student['course_name']}')

        except Exception as e:
            print(f'There was a non specific error')
            print('---Technical Error Message---')
            print(e, e.__doc__, type(e), sep='\n')

    # Exit program
    elif menu_choice == '4':
        print('Goodbye!')
        exit()

    # handles all other inputs
    else:
        print('Does not compute')
