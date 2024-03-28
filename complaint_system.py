# Complaint file
complaints_file = "complaints-list_1023.txt"

while True:

    choice = input(" ")

    if choice == '*127#':
        print("CITIZEN PORTAL")

    elif choice == '*127*300#':
        print("LEADER ADMIN VIEW PORTAL ")

    else:
        print("UNKNOWN APPLICATION")
        exit(0)
