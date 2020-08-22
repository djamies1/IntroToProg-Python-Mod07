# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple program to create a list of customer data prompted from the user
#              who can save or read data to a binary file.
# ChangeLog: (Who, When, What)
# <David Jamieson>,<8/20/2020>,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []
lstNew = []
strId = ""
strName = ""
strChoice = ""

# Processing -------------------------------------- #


def save_data_to_file(file_name, list_of_data):
    pass  # TODO: Add code here
    with open(file_name, 'wb') as file:
        pickle.dump(list_of_data, file)
    print('Data saved to file!')


def read_data_from_file(file_name):
    pass  # TODO: Add code here
    pickle_off = open(file_name, "rb")
    lstRead = pickle.load(pickle_off)
    print(lstRead)


# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object

def get_input_from_user():
    id = str(input("Please enter a Customer ID:"))
    name = str(input("Please enter a Customer NAME:"))
    return id, name


def add_input_to_list(id, name, list_of_rows):
    lstRow =[id, name]
    list_of_rows.append(lstRow)
    return list_of_rows


def print_menu_tasks():
    """  Display a menu of choices to the user

    :return: nothing
    """
    print('''
    Menu of Options
    1) Add a new customer to list
    2) Save Data to File     
    3) Read data from File
    4) Exit Program
        ''')
    print()  # Add an extra line for looks
    choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
    return choice

# Main Script ------------------------------------ #


try:

    print("Hello! This program will allow you to create a brand new list of customers and overwrite a binary file."
      " Please begin adding customers by selecting from the options below.")

    while True:
        strChoice = print_menu_tasks()

        if strChoice.strip() == '1':  # Add a new customer to the list
            strId, strName = get_input_from_user()
            add_input_to_list(strId, strName, lstCustomer)
            continue
        elif strChoice.strip() == '2':  # TODO: store the list object into a binary file
            save_data_to_file(strFileName, lstCustomer)
            continue
        elif strChoice.strip() == '3':  # TODO: Read the data from the file into a new list object and display the contents
            read_data_from_file(strFileName)
            continue
        elif strChoice.strip() == '4':  # Exit the program.
            print('Exiting program - thank you!')
            break
        else:
            print("Please select an option from [1 to 4].")
            continue

except Exception as e:
    print("There was an error! Please start the program again")
    print("The error was: ", e)
