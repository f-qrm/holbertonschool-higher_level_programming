#!/usr/bin/python3
"""
Script that connects to a MySQL database and retrieves all rows
from the `states` table where the name starts with the user-provided input.

Usage:
    ./2-my_filter_states.py <username> <password> <database> <state_name>

Arguments:
    username: MySQL username
    password: MySQL password
    database: Name of the MySQL database to use
    state_name: The name of the state to search for
    (exact match, case-sensitive)

Note:
    The script uses string formatting to build the SQL query
    (not secure for production).
    It connects to a MySQL server running on localhost at port 3306.
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
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE '{}%'"
                "ORDER BY id ASC".format(searched_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
