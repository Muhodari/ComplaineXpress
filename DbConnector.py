# DbConnector.py

import mysql.connector

def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("\n\t ")
        return connection
    except mysql.connector.Error as error:
        print("Failed to connect to the database:", error)
        return None
