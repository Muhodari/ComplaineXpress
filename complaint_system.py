# Complaint file
complaints_file = "complaints-list_1023.txt"

while True:
    print("****************************************")
    print("* Welcome to ComplineXpress System     *")
    print("****************************************")
    print("1. Register complaint                  *")
    print("2. View all complaint                  *")
    print("3. Delete complaint                    *")
    print("4. Respond to Complaint                *")
    print("5. Exit                                *")

    choice = input("Enter choice(1-5): ")

    if choice == '1':
    print("Register complaint ")
    complaint_id = input("Enter complaint ID: ")
    with open(complaints_file, 'r') as file:
        complaint_ids = [line.split(',')[1].strip() for line in file.readlines()]
    if complaint_id in complaint_ids:
        print("Complaint ID already exists")
    else:
        complaint_text = input("Enter your complaint: ")
        with open(complaints_file, 'a') as file:
            file.write(f"{complaint_text},{complaint_id}\n")
        print("Complaint registered successfully!")


    elif choice == '2':
       print("View all complains ")


    elif choice == '3':
       print("Delete complaints ")
 

    elif choice == '4':
       print("Respond complaints")


    elif choice == '5':
       print("Exit")
       break

    else:
       print("Invalid choice. Please enter a number from 1 to 5.")
