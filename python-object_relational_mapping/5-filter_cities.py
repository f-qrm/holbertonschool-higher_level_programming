#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password>
    <database_name> <state_name>

Arguments:
    mysql_username: MySQL server username (e.g. root)
    mysql_password: MySQL server password
    database_name:  Name of the MySQL database to use
    state_name:     Name of the state whose cities you want to list

Output:
    Displays city names (only) from the specified state,
    ordered by city ID ascending, separated by commas.

Example:
    ./5-filter_cities.py root root hbtn_0e_4_usa California
    San Francisco, Los Angeles, San Diego
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_DB = sys.argv[3]
    name_state = sys.argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=name_DB,
        port=3306
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (name_state,)
    )
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    conn.close()
