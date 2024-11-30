# Swayam Shree
# 9/14/2024
# main file for contact list program

from contacts import *

contactList = []

while(True):
    print("\n     *** EMPLOYEE CONTACT MAIN MENU          \n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program\n")

    menu = input("\nEnter menu choice: ")

    if menu == '1':
        print_list(contactList)
    elif menu == '2':
        add_contact(contactList, firstName= input("Enter first name: "), lastName= input("Enter last name: "))
    elif menu == '3':
        try:
            index = int(input("Enter the index number: "))
            if not modify_contact(contactList, index=index, firstName=input("Enter first name: "), lastName=input("Enter last name: ")):
                print("Invalid index number.")
        except ValueError:
            print("Please enter a valid numeric index.")

    elif menu == '4':
        try:
            index = int(input("Enter the index number: "))
            if not delete_contact(contactList, index=index):
                print("Invalid index number.")
        except ValueError:
            print("Please enter a valid numeric index.")

    elif menu == '5':
        sort_contacts(contactList, column=0)
    elif menu == '6':
        sort_contacts(contactList, column=1)
    elif menu == '7':
        break
    else:
        print("Invalid Command")
