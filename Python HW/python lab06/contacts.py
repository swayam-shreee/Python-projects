import json


class Contacts:

    id = 0
    first_name = ''
    last_name = ''
    data = {}


    def __init__(self, *, filename):

        self.filename = filename
        self.data = {}

        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Starting with an empty contact list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from '{self.filename}'. Starting with an empty contact list.")



    def add_contact(self, *, id, first_name, last_name):
        """Add a new contact to the contact list."""
        if id in self.data:
            return "error"

        self.data[id] = [first_name, last_name]
        # Sort the dictionary by last name and first name
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        # Write the updated dictionary to the file
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        
        return {id: self.data[id]}

    
    def modify_contact(self, *, id, first_name, last_name):
        """Modify an existing contact in the contact list."""
        if id not in self.data:
            return "error"

        self.data[id] = [first_name, last_name]
        # Sort the dictionary by last name and first name
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
        # Write the updated dictionary to the file
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        
        return {id: self.data[id]}

    def delete_contact(self, *, id):
        """Delete a contact from the contact list."""
        if id not in self.data:
            return "error"

        deleted_contact = {id: self.data[id]}

        del self.data[id]
        # Write the updated dictionary to the file
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        
        return deleted_contact