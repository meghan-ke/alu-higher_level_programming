"""
This script connects to a MySQL server and creates the database 'hbtn_0c_0'.
If the database already exists, the script will not fail due to 'IF NOT EXISTS'.
It does not use SELECT or SHOW statements.
"""

import mysql.connector

def create_hbtn_0c_0_database():
    """
    Connects to a MySQL server and creates the database 'hbtn_0c_0'
    if it does not already exist.
    """
    # --- MySQL Connection Configuration ---
    # IMPORTANT: You MUST replace 'your_mysql_username' and 'your_mysql_password'
    # with your actual MySQL server credentials.
    # The user needs sufficient privileges to CREATE DATABASES.
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
        # Establish the connection to the MySQL server
        # Note: We connect without specifying a database initially,
        # as we are creating a new one.
        print(f"Attempting to connect to MySQL server at {DB_CONFIG['host']}...")
        connection = mysql.connector.connect(**DB_CONFIG)
        print("Successfully connected to MySQL server.")

        # Create a cursor object for executing SQL queries
        cursor = connection.cursor()

        # SQL query to create the database if it doesn't already exist.
        # SQL keywords are in uppercase as good practice.
        create_db_query = "CREATE DATABASE IF NOT EXISTS hbtn_0c_0"
        
        print(f"Executing query: '{create_db_query}'...")
        cursor.execute(create_db_query)
        
        # Commit the changes to the database
        connection.commit()
        print("Database 'hbtn_0c_0' created successfully or already exists.")

    except mysql.connector.Error as err:
        # Handle specific MySQL connection and query errors
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied for user. Please check your MySQL username and password. "
                  "Ensure the user has CREATE DATABASE privileges.")
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
    create_hbtn_0c_0_database()
