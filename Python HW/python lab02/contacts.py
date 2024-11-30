
# Swayam Shree
# 9/14/2024
# function declaration for employee contact list

contactList = [["swayam", "shree"], ["luke", "gonz"], ["steph", "williams"]]

# prints list
def print_list(contacts : list):
    """ prints entire contact list """

    print("================ CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ==================")

    for i in range(len(contacts)):        
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
    

# add contact
def add_contact(contact: list, /, *, firstName, lastName):
    """ adds a contact"""
    contact.append([firstName, lastName])
    return contact


# modify contact
def modify_contact(contact: list, /, *, firstName, lastName, index):
    """modify contact"""
    if index >= len(contact):
        return False

    contact[index][0] = firstName
    contact[index][1] = lastName

    return True

# delete contact
def delete_contact(contact: list, /, *, index):
    """ deletes contact"""
    if index >= len(contact):
        return False

    del contact[index]
    return True

def sort_contacts(contact, /, *, column):
    if column == 0:
        contact.sort(key= lambda x: x[0])
    elif column == 1:
        contact.sort(key= lambda x: x[1])


