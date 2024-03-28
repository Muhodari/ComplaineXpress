# Complaint file
complaints_file = "complaints-list_1023.txt"
def leadermenu():
    print("Leader Options:")
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
        print("LEADER ADMIN VIEW PORTAL ")

    else:
        print("UNKNOWN APPLICATION")
        exit(0)
