# Complaint file
from colorama import init, Fore, Style
complaints_file = "complaints-list_1023.txt"

def all_sectors_choice():
    print("\tAll sectors  ")
    while True:
        print("\t1. Sector A")
        print("\t2. Sector B")
        print("\t3. Sector C")
        print("\t4. Return to main menu")

        choice = input("Enter choice: ")

        if choice == '1':
            department("Sector A")
        elif choice == '2':
            department("Sector B")
        elif choice == '3':
            department("Sector C")
        elif choice == '4':
            print("Returning to main menu")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

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
            print("Returning to All sectors choice")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def complain(department):
    print("\n")
    print(f"=> Complain to  {department}")
    complaint_text = input("Enter your complaint: ")
    print("Complaint submitted successfully!")
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
            print("CITIZEN PORTAL")
            all_sectors_choice()

        elif choice == '*127*300#':
            print("LEADER ADMIN VIEW PORTAL ")

        else:
            print("UNKNOWN APPLICATION")
            exit(0)
