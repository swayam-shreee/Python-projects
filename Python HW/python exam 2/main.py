from people import Person, CSUF_Student

def main():
    
    bob = Person('Bob', 'Smith', 'Male', '25')
    print(bob.getName())
    print()

    ken = Person('Ken', 'Johnson', 'Male', '25')

    swayam = CSUF_Student('Swayam', 'Shree', 'Male' , '19', '12345', 'Computer Science')
    print(swayam.getName())
    print(swayam.getID())
    print(swayam.major)
    swayam.changeMajor('Computer Engineering')
    print(swayam.major)
    print(CSUF_Student.counter)
    print(CSUF_Student.address)

    kat = CSUF_Student('kat', 't', 'Female' , '19', '123', 'Computer Science')
    print(kat.counter)





if __name__ == '__main__':
    main()
