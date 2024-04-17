from colorama import init, Fore, Style
from DbConnector import connect_to_database
from tabulate import tabulate

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

        choice = input("Enter department: ")

        if choice == '1':
            complain("Department 1", sector)
        elif choice == '2':
            complain("Department 2", sector)
        elif choice == '3':
            complain("Department 3", sector)
        elif choice == '4':
            print("\tReturning to All sectors choice")
            break
        else:
            print("\tInvalid choice. Please enter a number from 1 to 4.")


def complain(department, sector):
    global cursor
    print("\n")
    print(f"=> Complain to  {department}")
    sector_id = 20
    sector_name = sector
    department_id = 10
    department_name = department
    complain_text = input("Enter complain: ")
    phone_number = input("Enter phone number: ")
    email_address = input("Enter email address: ").lower()
    status = 'PENDING'
    db_connection = connect_to_database("localhost", "root", "root", "complain_express")
    try:
        cursor = db_connection.cursor()
        sql = "INSERT INTO Complain (sector_id, sector_name, department_id, department_name, complain_text, phone_number, email_address, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (sector_id, sector_name, department_id, department_name, complain_text, phone_number, email_address, status))
        db_connection.commit()
        print("Complain submitted successfully!")
    except Exception as e:
        print(f"Error inserting data into the database: {e}")
    finally:
        cursor.close()
        db_connection.close()
    print("\tComplain submitted successfully!")
    exit(0)

def read_complaint_by_id(complaint_id):
    global cursor
    try:
        sql = "SELECT * FROM Complain WHERE id = %s"
        cursor.execute(sql, (complaint_id,))
        complaint = cursor.fetchone()
        if complaint:
            print("Complaint found:")
            headers = ["ID", "Sector ID", "Sector Name", "Department ID", "Department Name", "Complain Text", "Phone Number", "Email Address", "Status"]
            data = [[complaint[0], complaint[1], complaint[2], complaint[3], complaint[4], complaint[5], complaint[6], complaint[7], complaint[8]]]
            table = tabulate(data, headers=headers, tablefmt="pretty")
            print(table)
        else:
            print("Complaint not found.")
    except Exception as e:
        print(f"Error reading data from the database: {e}")
def read_all_complaints():
    global cursor
    try:
        sql = "SELECT * FROM Complain"
        cursor.execute(sql)
        complaints = cursor.fetchall()
        if complaints:
            print("All complaints found:")
            headers = ["ID", "Sector ID", "Sector Name", "Department ID", "Department Name", "Complain Text", "Phone Number", "Email Address", "Status"]
            data = [[c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]] for c in complaints]
            table = tabulate(data, headers=headers, tablefmt="pretty")
            print(table)
        else:
            print("No complaints found.")
    except Exception as e:
        print(f"Error reading data from the database: {e}")



# Entry point of the program
if __name__ == "__main__":
    db_connection = connect_to_database("localhost", "root", "root", "complain_express")
    if db_connection is not None:
        # Create a cursor object
        cursor = db_connection.cursor()
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
                        print("4. all")
                        print("5. get by Id")

                        complaint_status = input("Enter status choice: ")

                        if complaint_status == '1':
                            print("Displaying approved complaints")

                        elif complaint_status == '2':
                            print("Displaying ignored complaints")

                        elif complaint_status == '3':
                            print("Displaying pending complaints")
                        elif complaint_status == '4':
                            print("Displaying all\n\n")
                            read_all_complaints()
                        elif complaint_status == '5':
                            complainId = input("Enter complaint id: ")
                            read_complaint_by_id(complainId)
                        else:
                            print("Invalid status choice")
                            exit(0)

            else:
                print("Invalid sub-choice")
                exit(0)

        else:
            print("UNKNOWN APPLICATION")
            exit(0)
