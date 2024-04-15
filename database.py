# database.py

import mysql.connector

def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("\n\t Connected to the database successfully")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to the database:", error)
        return None
