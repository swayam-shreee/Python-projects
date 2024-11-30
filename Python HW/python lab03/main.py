# Swayam Shree
# 9/24/2024
# main file for contact list program

from contacts import *

contactDict = dict()

while(True):
    print("\n     *** EMPLOYEE CONTACT MAIN MENU          \n")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print Contact List")
    print("5. Find contact")
    print("6. Exit the program")


    menu = input("\nEnter menu choice: ")
        
    if menu == '1':
        try:
            id = int(input("Enter phone number: "))
            if not add_contact(contactDict, id=id, firstName=input("Enter first name: "), lastName=input("Enter last name: ")):
                print("Invalid phone number.")
        except ValueError:
            print("Please enter a valid numeric index.")
    elif menu == '2':
        try:
            id = int(input("Enter phone number: "))
            if not modify_contact(contactDict, id=id, firstName=input("Enter first name: "), lastName=input("Enter last name: ")):
                print("Invalid phone number.")
        except ValueError:
            print("Please enter a valid numeric index.")
    elif menu == '3':
        try:
            id = int(input("Enter phone number: "))
            if not delete_contact(contactDict, id=id):
                print("Invalid phone number.")
        except ValueError:
            print("Please enter a valid numeric index.")
    elif menu == '4':
        print_list(contactDict)
    elif menu == '5':
        print_list(find_contact(contactDict, find= input("Enter search string: ")))
    elif menu == '6':
        break
    else:
        print("Invalid Command")




    
