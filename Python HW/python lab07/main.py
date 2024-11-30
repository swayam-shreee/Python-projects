from people import Faculty, Student

def main():
    faculty_list = []
    student_list = []

    while True:
        print("\n*** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
        print("1. Add faculty")
        print("2. Print faculty")
        print("3. Add student")
        print("4. Print student")
        print("9. Exit the program\n")
        choice = input("Enter menu choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            department = input("Enter department: ")
            faculty = Faculty(first_name, last_name, department)
            faculty_list.append(faculty)
        elif choice == '2':
            print("\n===================== FACULTY ===========================")
            print("Record  Name                  Department")
            print("======  ====================  ===========================")
            for index, faculty in enumerate(faculty_list):
                print(f"{index:<7} {faculty.firstname + ' ' + faculty.lastname:<21} {faculty.department}")
        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            class_year = input("Enter class year: ")
            major = input("Enter major: ")
            advisor_index = input("Enter faculty advisor: ")

            if advisor_index.isdigit():
                advisor_index = int(advisor_index)
                if 0 <= advisor_index < len(faculty_list):
                    advisor = faculty_list[advisor_index]
                    student = Student(first_name, last_name)
                    student.set_class(class_year)
                    student.set_major(major)
                    student.set_advisor(advisor)
                    student_list.append(student)
                else:
                    print("Invalid faculty index.")
            else:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("\n===================================== STUDENTS =========================================")
            print("Name                  Class      Major                      Advisor")
            print("====================  =========  =========================  ============================")
            for student in student_list:
                print(f"{student.firstname + ' ' + student.lastname:<21} {student.classyear:<10} {student.major:<26} {student.advisor.firstname + ' ' + student.advisor.lastname}")
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    