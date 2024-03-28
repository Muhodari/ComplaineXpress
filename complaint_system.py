
from colorama import init, Fore, Style
complaints_file = "complaints-list_1023.txt"

def all_sectors_choice():
    print("\tAll sectors  ")
    while True:
        print("\t1. Sector A")
        print("\t2. Sector B")
        print("\t3. Sector C")
        print("\t4. Return to main menu")

        choice = input("Enter sector: ")

        if choice == '1':
            department("Sector A")
        elif choice == '2':
            department("Sector B")
        elif choice == '3':
            department("Sector C")
        elif choice == '4':
            print("\tReturning to main menu")
            break
        else:
            print("\tInvalid choice. Please enter a number from 1 to 4.")

def department(sector):
    print(f"=> Departments in {sector}")
    while True:
        print("\t1. Department 1")
        print("\t2. Department 2")
        print("\t3. Department 3")
        print("\t4. Return to All sectors choice")

        choice = input("Enter choice: ")

        if choice == '1':
            complain("Department 1")
        elif choice == '2':
            complain("Department 2")
        elif choice == '3':
            complain("Department 3")
        elif choice == '4':
            print("\tReturning to All sectors choice")
            break
        else:
            print("\tInvalid choice. Please enter a number from 1 to 4.")

def complain(department):
    print("\n")
    print(f"=> Complain to  {department}")
    complaint_text = input("Enter your complaint: ")
    print("\tComplaint submitted successfully!")
    exit(0)

# Entry point of the program
if __name__ == "__main__":
    while True:
        init()
        print(Fore.GREEN + '''
                  Complain
                /       Express
                |        |
                |        |
                |________|
        ''' + Style.RESET_ALL)

        choice = input(" ")

        if choice == '*127#':
            print("\tCITIZEN PORTAL")
            all_sectors_choice()

        elif choice == '*127*300#':
            print("LEADER ADMIN VIEW PORTAL")
            print("1. Admin")
            print("2. Leader")

            sub_choice = input("Enter portal choice: ")

            if sub_choice == '1':
                print("Admin Portal")
                # Add admin functionalities here

            elif sub_choice == '2':
                 print("Leader Portal")
                 print("1. View Complaints")

                 leader_choice = input("Enter leader choice: ")

                 if leader_choice == '1':
                    print("1. Approved")
                    print("2. Ignored")
                    print("3. Pending")
                
                    complaint_status = input("Enter status choice: ")

                    if complaint_status == '1':
                        print("Displaying approved complaints")

                    elif complaint_status == '2':
                        print("Displaying ignored complaints")

                    elif complaint_status == '3':
                        print("Displaying pending complaints")

                    else:
                        print("Invalid status choice")
                        exit(0)

        else:
            print("Invalid sub-choice")
            exit(0)

    else:
        print("UNKNOWN APPLICATION")
        exit(0)
i
