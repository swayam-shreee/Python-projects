
# Swayam Shree
# 9/5/2024
# function declaration for employee contact list


# prints list
def print_list(contacts : list):
    """ prints entire contact list """

    print("================== CONTACT LIST ================")
    print("Index   First Name            Last Name")
    print("======  ====================  ==================")

    for i in range(len(contacts)):        
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
    

# add contact
def add_contact(contact: list):
    """ adds a contact"""
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")

    contact.append([firstName, lastName])
    return contact

# modify contact
def modify_contact(contact: list):
    """modify contact"""
    index = int(input("Enter the index number: "))
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")

    contact[index][0] = firstName
    contact[index][1] = lastName
    return contact

# delete contact
def delete_contact(contact: list):
    """ deletes contact"""
    index = int(input("Enter the index number: "))

    del contact[index]
    return contact


