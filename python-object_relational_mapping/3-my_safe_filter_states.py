#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all rows
from the `users` table where the `name` column matches the given user
input exactly.

Usage:
    ./your_script_name.py <mysql_username> <mysql_password> <database_name>
    <searched_name>

Arguments:
    mysql_username: The username used to authenticate with the MySQL server
    mysql_password: The password for the given username
    database_name: The name of the database containing the `users` table
    searched_name: The exact name to search for in the `users` table

Features:
    - Uses the MySQLdb library for MySQL connection
    - Connects to localhost on port 3306
    - Uses parameterized queries to avoid SQL injection
    - Displays all matching rows, one per line

Example:
    $ ./your_script.py root root my_database 'Alice'
    (1, 'Alice')
    (7, 'Alice')
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_DB = sys.argv[3]
    searched_name = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=name_DB,
        port=3306
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s", (searched_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
