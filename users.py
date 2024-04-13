import sqlite3
from colorama import init, Fore, Style

# Create or connect to the SQLite database
conn = sqlite3.connect('complaints_database.db')
cursor = conn.cursor()

# Create a table to store user credentials if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    role TEXT
                )''')
conn.commit()

# Create a table to store complaints if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS complaints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    sector TEXT,
                    department TEXT,
                    complaint_text TEXT,
                    status TEXT DEFAULT 'Pending'
                )''')
conn.commit()

def register_user(username, password, role):
    try:
        cursor.execute('''INSERT INTO users (username, password, role)
                        VALUES (?, ?, ?)''', (username, password, role))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")

def login_user(username, password):
    cursor.execute('''SELECT * FROM users WHERE username=? AND password=?''',
                   (username, password))
    user_data = cursor.fetchone()
    if user_data:
        print(f"Login successful! Welcome, {username}.")
        return user_data[3]  # Return the role of the logged-in user
    else:
        print("Invalid username or password.")
        return None

def view_complaints(username, status):
    cursor.execute('''SELECT * FROM complaints WHERE username=? AND status=?''',
                   (username, status))
    complaints = cursor.fetchall()
    if complaints:
        print(f"Showing {status} complaints for {username}:")
        for complaint in complaints:
            print(f"Complaint ID: {complaint[0]}")
            print(f"Department: {complaint[3]}")
            print(f"Complaint: {complaint[4]}")
            print("-------------")
    else:
        print("No complaints found.")

def submit_complaint(username, sector, department, complaint_text):
    cursor.execute('''INSERT INTO complaints (username, sector, department, complaint_text)
                    VALUES (?, ?, ?, ?)''', (username, sector, department, complaint_text))
    conn.commit()
    print("Complaint submitted successfully!")

def approve_complaint(complaint_id):
    cursor.execute('''UPDATE complaints SET status='Approved' WHERE id=?''', (complaint_id,))
    conn.commit()
    print("Complaint approved successfully.")

def ignore_complaint(complaint_id):
    cursor.execute('''UPDATE complaints SET status='Ignored' WHERE id=?''', (complaint_id,))
    conn.commit()
    print("Complaint ignored.")

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
            sector = input("Enter your sector: ")
            department = input("Enter your department: ")
            complaint_text = input("Enter your complaint: ")
            # Assuming the logged-in user's username is stored in the variable 'username'
            submit_complaint(username, sector, department, complaint_text)

        elif choice == '*127*300#':
            print("LEADER ADMIN VIEW PORTAL")
            print("1. Login")
            print("2. Register")
            print("3. Exit")

            sub_choice = input("Enter portal choice: ")

            if sub_choice == '1':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                role = login_user(username, password)
                if role:
                    if role == 'admin':
                        print("Admin Portal")
                        while True:
                            print("1. Add User")
                            print("2. Register User")
                            print("3. Lock User")
                            print("4. Delete User")
                            print("5. Update User")
                            print("6. View User")
                            print("7. Create Sector")
                            print("8. Edit Sector")
                            print("9. Delete Sector")
                            print("10. View Sector")
                            print("11. Create Department")
                            print("12. Edit Department")
                            print("13. View Department")
                            print("14. Delete Department")
                            print("15. Logout")

                            admin_choice = input("Enter admin choice: ")

                            if admin_choice == '1':
                                print("Add User functionality")
                                # Implement Add User functionality here
                            elif admin_choice == '2':
                                print("Register User functionality")
                                # Implement Register User functionality here
                            elif admin_choice == '3':
                                print("Lock User functionality")
                                # Implement Lock User functionality here
                            elif admin_choice == '4':
                                print("Delete User functionality")
                                # Implement Delete User functionality here
                            elif admin_choice == '5':
                                print("Update User functionality")
                                # Implement Update User functionality here
                            elif admin_choice == '6':
                                print("View User functionality")
                                # Implement View User functionality here
                            elif admin_choice == '7':
                                print("Create Sector functionality")
                                # Implement Create Sector functionality here
                            elif admin_choice == '8':
                                print("Edit Sector functionality")
                                # Implement Edit Sector functionality here
                            elif admin_choice == '9':
                                print("Delete Sector functionality")
                                # Implement Delete Sector functionality here
                            elif admin_choice == '10':
                                print("View Sector functionality")
                                # Implement View Sector functionality here
                            elif admin_choice == '11':
                                print("Create Department functionality")
                                # Implement Create Department functionality here
                            elif admin_choice == '12':
                                print("Edit Department functionality")
                                # Implement Edit Department functionality here
                            elif admin_choice == '13':
                                print("View Department functionality")
                                # Implement View Department functionality here
                            elif admin_choice == '14':
                                print("Delete Department functionality")
                                # Implement Delete Department functionality here
                            elif admin_choice == '15':
                                print("Logging out...")
                                break
                            else:
                                print("Invalid admin choice")

                    elif role == 'leader':
                        print("Leader Portal")
                        while True:
                            print("1. View Complaints")
                            print("2. Approve Complaint")
                            print("3. Ignore Complaint")
                            print("4. Logout")

                            leader_choice = input("Enter leader choice: ")

                            if leader_choice == '1':
                                status_choice = input("Enter status choice (Approved/Ignored/Pending): ")
                                view_complaints(username, status_choice)
                            elif leader_choice == '2':
                                complaint_id = input("Enter complaint ID to approve: ")
                                approve_complaint(complaint_id)
                            elif leader_choice == '3':
                                complaint_id = input("Enter complaint ID to ignore: ")
                                ignore_complaint(complaint_id)
                            elif leader_choice == '4':
                                print("Logging out...")
                                exit(0)
                            else:
                                print("Invalid leader choice")
                                exit(0)

                        else:
                            print("Unknown role")
                            exit(0)
                    else:
                        print("Login failed")
                        exit(0)

                elif sub_choice == '2':
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    role = input("Enter your role (admin/leader): ")
                    register_user(username, password, role)

                elif sub_choice == '3':
                    print("Exiting...")
                    break

                else:
                    print("Invalid sub-choice")
                    exit(0)

            else:
                print("Invalid choice")
                exit(0)


