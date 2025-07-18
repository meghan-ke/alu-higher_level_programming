#!/usr/bin/python3
# This script lists all databases of the MySQL server using the MySQLdb module

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect using credentials passed via command line
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2]
    )
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES")

    # Sort and print databases
    databases = sorted([row[0] for row in cursor])
    for db_name in databases:
        print(db_name)

    cursor.close()
    db.close()
