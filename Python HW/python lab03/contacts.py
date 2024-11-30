
# Swayam Shree
# 9/24/2024
# function declaration for employee contact list


# prints list
def print_list(contacts : dict()):
    """ prints entire contact list """

    print("================ CONTACT LIST ==================")
    print("First Name          Last Name           Phone")
    print("===============  ===============  ===============")

    for k, v in contacts.items():
        print(f'{v[0]:16}  {v[1]:10}  {k:16}')
    

# add contact
def add_contact(contact: dict, /, *, id, firstName, lastName):
    """ adds a contact"""
    if id in contact:
        return "error"
        
    contact[id] = [firstName, lastName]
    return contact[id]


# modify contact
def modify_contact(contact: dict, /, *, id, firstName, lastName):
    """modify contact"""
    if id not in contact:
        return "error"

    contact[id] = [firstName, lastName]
    return contact[id]

# delete contact
def delete_contact(contact: dict, /, *, id):
    """ deletes contact"""
    if id not in contact:
        return "error"

    temp = contact[id]
    del contact[id]
    return temp

#sort contacts
def sort_contacts(contacts):
    """Sort the contacts by last name, then by first name"""
    sorted_contacts = dict(sorted(contacts.items(), key=lambda x: (x[1][1], x[1][0])))
    return sorted_contacts

#find contact
def find_contact(contacts, *, find=None):
    """Find the contacts by phone number or first or last name"""
    found_contacts = {}

    if find and find.isdigit() and find in contacts:
        found_contacts[find] = contacts[find]

    for phone, name in contacts.items():
        first_name, last_name = name
        if find and (find.lower() in first_name.lower() or find.lower() in last_name.lower()):
            found_contacts[phone] = name

    sorted_found_contacts = sort_contacts(found_contacts)

    return sorted_found_contacts







