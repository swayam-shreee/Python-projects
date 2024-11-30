
class MyTypeError(Exception):
    pass


class Person:
    def __init__(self, first_name, last_name, gender, age):
        #error handling
        if not age.isdigit():
            raise ValueError('Age must be a number')
        if gender not in ['Male', 'Female']:
            raise MyTypeError('Gender must be "male" or "female"')
        
        #instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.first_name + ' ' + self.last_name


class CSUF_Student(Person):
    counter = 0
    address = '800 N State College Blvd, Fullerton, CA 92831'

    def __init__(self, first_name, last_name, gender, age, ID, major):
        #error handling
        if not ID.isdigit():
            raise ValueError('ID must be a number')

        #instance variables
        super().__init__(first_name, last_name, gender, age)
        self.ID = ID
        self.major = major

        CSUF_Student.counter += 1     # increment counter

    def getID(self):
        return self.ID
    
    def changeMajor(self, new_major):
        self.major = new_major
    
    def getName(self):
        return self.first_name + ' ' + self.last_name + '       ID: ' + self.ID

