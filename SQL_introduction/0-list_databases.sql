#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all available databases.
It adheres to the following requirements:
- Starts with a shebang and module-level comments.
- Uses uppercase for SQL keywords.
- Ensures the output list of databases is sorted alphabetically.
- Dynamically lists databases, reflecting any new creations.

Before running:
1. Install mysql-connector-python: pip install mysql-connector-python
2. Replace 'your_mysql_username' and 'your_mysql_password' with your actual credentials.
"""

import mysql.connector

def list_mysql_databases():
    """
    Connects to a MySQL server and prints a list of all databases.
    The output databases will be sorted alphabetically.
    """
    # --- MySQL Connection Configuration ---
    # IMPORTANT: You MUST replace 'your_mysql_username' and 'your_mysql_password'
    # with your actual MySQL server credentials.
    # For production environments, consider using environment variables or a secure
    # configuration file instead of hardcoding sensitive information.
    DB_CONFIG = {
        'host': 'localhost',  # Often 'localhost', or the IP address/hostname of your MySQL server
        'user': 'your_mysql_username', # Your MySQL username (e.g., 'root')
        'password': 'your_mysql_password', # Your MySQL password
        # 'port': 3306 # Uncomment and change if your MySQL server uses a non-default port
    }

    connection = None # Initialize connection variable to None
    cursor = None     # Initialize cursor variable to None

    try:
        # Attempt to establish a connection to the MySQL server
        print(f"Attempting to connect to MySQL server at {DB_CONFIG['host']}...")
        connection = mysql.connector.connect(**DB_CONFIG)
        print("Successfully connected to MySQL server.")

        # Create a cursor object for executing SQL queries
        cursor = connection.cursor()

        # Execute the SQL query to retrieve all database names.
        # SQL keywords are in uppercase as required.
        print("Executing 'SHOW DATABASES' query...")
        cursor.execute("SHOW DATABASES")

        # Fetch all results from the query
        databases = cursor.fetchall()

        # Process and print the list of databases
        if databases:
            # Extract database names and sort them alphabetically as required.
            database_names = sorted([db_tuple[0] for db_tuple in databases])
            
            print("\n--- Databases on your MySQL server ---")
            for db_name in database_names:
                print(f"- {db_name}")
            print("--------------------------------------")
        else:
            print("No databases found or accessible with the provided credentials.")

    except mysql.connector.Error as err:
        # Handle specific MySQL connection and query errors
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied for user. Please check your MySQL username and password.")
        elif err.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
            print(f"Error: Could not connect to MySQL host '{DB_CONFIG['host']}'. "
                  "Ensure the MySQL server is running and accessible from this machine.")
        else:
            print(f"An unexpected MySQL error occurred: {err}")
    except Exception as e:
        # Catch any other general exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the cursor and connection are closed properly in all cases
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    list_mysql_databases()
