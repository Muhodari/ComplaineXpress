# Complaint file
complaints_file = "complaints-list_1023.txt"
def leadermenu():
    print("Leader Portal:")
    print("1. View Complaints")
    print("2. Approve")
    print("3. Ignore")
    print("4. Logout")
    print("5. Exit")
while True:

    choice = input("choice: i")

    if choice == '*127#':
        print("CITIZEN PORTAL")

    elif choice == '*127*300#':
        print("LEADER ADMIN VIEW PORTAL")
        print("1. Admin")
        print("2. Leader")

        sub_choice = input("Enter portal choice: ")

        if sub_choice == '1':
            print("Admin Portal")
            # Add admin functionalities here

        elif sub_choice == '2':
            leadermenu()

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
        elif leader_choice = '2':
            print("Approving the complaint")
        elif leader_choice = '3':
            print("ignoring complaint")
        elif leader_choice = '4':
            print("Thank you for using Complain express")
            exit(0)
        else:
            print("Invalid sub-choice")
            exit(0)

    else:
        print("UNKNOWN APPLICATION")
        exit(0)

