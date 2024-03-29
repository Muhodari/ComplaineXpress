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
		admin_portal()

	    elif sub_choice == '2':
		leader_portal()
	    else
		print("invalid choice")
	else
	    print("UNKOWN APPLICATION")

def admin_portal():
    print("Admin Portal")
    # Add admin functionalities here
    print("1. manage users")
    print("2. manage sectors")
    print("3. manage departments")
    print("4. logout")

    admin_choice = input("Enter admin choice")

    if admin_choice == '1':
        print("1. Register user")
        print("2. Lock user")
        print("3. delete user")
        print("4. update user")
        print("5. view user")

	user_choice = input("Enter choice")

	if user_choice == '1':
	    username = input("Enter username: ")
	    print(f"user {username} registered successifuly")
	elif user_choice == '2':
	    username = input("Enter username to Lock: ")
	    print(f"user {username} locked")
	elif user_choice == '3':
	    username = input("ENter username to delete: ")
	    print(f"user {username} deleted")
	elif user_choice == '4':
	    username = input("Enter username")
	    print("user updated")
	elif user_choice == '5':
	    print("user view")
	else
	    print("invalid choice")
    elif admin_choice == '2':
        print("1. create sector")
        print("2. edit sector")
        print("3. delete sector")
        print("4. view sector")

	sector_choice = input("Enter choice")

        if sector_choice == '1':
            sectorname = input("Enter sector: ")
            print("sector created successifuly")
        elif user_choice == '2':
            sectorname = input("Enter sector: ")
            print("sector edited")
        elif sector_choice == '3':
            sectorname = input("Enter sector to delete: ")
            print("sector deleted")
        elif sector_choice == '4':
            print("sector view")
	else
	    print("invalid choice")

    elif admin_choice == '3':
        print("1. create department")
        print("2. edit department")
        print("3. delete department")
        print("4. view department")

	depart_choice = input("Enter choice")

        if depart_choice == '1':
            departname = input("Enter department: ")
            print("department created successifuly")
        elif depart_choice == '2':
            departname = input("Enter department: ")
            print("department edited")
        elif depart_choice == '3':
            departname = input("Enter department to delete: ")
            print("department deleted")
        elif depart_choice == '4':
            print("department view")
        else
            print("invalid choice")
    elif admin_choice == '4':
        print("logging out")
	exit(0)
    else
	print("invalid choice")

def leader_portal():
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
          exit(0)

       elif complaint_status == '2':
          print("Displaying ignored complaints")
          exit(0)

          elif complaint_status == '3':
          print("Displaying pending complaints")
          exit(0)

          else:
          print("Invalid status choice")
          exit(0)

    else:
        print("Invalid sub-choice")
        exit(0)

    else:
        print("UNKNOWN APPLICATION")
        exit(0)

