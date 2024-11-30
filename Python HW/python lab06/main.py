import json
from contacts import Contacts


def display_menu():
    print("\n*** TUFFY TITAN CONTACT MAIN MENU ***")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Set contact filename")
    print("6. Exit the program\n")
    

def print_contact_list(contacts):
    print("==================== CONTACT LIST ====================")
    print("Last Name            First Name           Phone")
    print("==================== ==================== ============")
    for id, (first_name, last_name) in contacts.data.items():
        print(f"{last_name:<20} {first_name:<20} {id}")
    print("")

def main():
    # Instantiate the Contacts object with a default filename
    filename = "contacts.json"
    contacts = Contacts(filename=filename)

    while True:
        display_menu()
        choice = input("Enter menu choice: ")
        print()


        if choice == '1':  # Add contact
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.add_contact(id=id, first_name=first_name, last_name=last_name)

            if result == "error":
                print("Phone number already exists.")
            else:
                print(f"Added: {first_name} {last_name}.")

        elif choice == '2':  # Modify contact
            id = input("Enter phone number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contacts.modify_contact(id=id, first_name=first_name, last_name=last_name)
            
            if result == "error":
                print("Phone number already exists.")
            else:
                print(f"Modified: {first_name} {last_name}.")

        elif choice == '3':  # Delete contact
            id = input("Enter phone number: ")
            result = contacts.delete_contact(id=id)
            if result == "error":
                print("Invalid phone number.")
            else:
                deleted_contact = result
                print(f"Deleted: {deleted_contact[id][0]} {deleted_contact[id][1]}.")

        elif choice == '4':  # Print contact list
            print_contact_list(contacts)

        elif choice == '5':  # Set contact filename
            filename = input("Enter new filename: ")
            contacts = Contacts(filename=filename)  # Re-instantiate with the new filename

        elif choice == '6':  # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()