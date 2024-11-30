# Swayam Shree
# 9/5/2024
# main file for contact list program

from contacts import *

contactList = []

while(True):
    print("\n     *** EMPLOYEE CONTACT MAIN MENU          \n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Exit the program\n")

    menu = int(input("\nEnter menu choice: "))

    if menu == 1:
        print_list(contactList)
    elif menu == 2:
        add_contact(contactList)
    elif menu == 3:
        modify_contact(contactList)
    elif menu == 4:
        delete_contact(contactList)
    elif menu == 5:
        break
    else:
        print("Invalid Command")
