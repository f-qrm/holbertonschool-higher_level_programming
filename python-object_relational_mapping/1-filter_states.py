#!/usr/bin/python3
"""
Script that lists all states from a MySQL database whose names start with 'N'.

This script connects to a MySQL database using credentials provided as
command-line arguments and retrieves all rows from the `states` table
where the name starts with 'N'.
The comparison is case-sensitive due to the use of the BINARY keyword
in the SQL query.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The name of the MySQL database to connect to.

Example:
    ./0-select_states.py root root123 hbtn_0e_0_usa

Requirements:
    - MySQL server must be running on localhost with port 3306.
    - The `MySQLdb` module (from `mysqlclient` package) must be installed.

Note:
    This script should not be executed if imported as a module.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_DB = sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=name_DB,
        port=3306
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    conn.close()
