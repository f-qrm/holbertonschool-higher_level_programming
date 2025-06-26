#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all rows
from the 'states' table, ordered by ascending ID.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The MySQL username to connect with.
    mysql_password: The corresponding password for the user.
    database_name : The name of the database to connect to.

Requirements:
    - The MySQL server must be running on localhost at port 3306.
    - The 'states' table must exist in the specified database.
    - The MySQLdb module must be installed (use `pip install mysqlclient`).
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    name_DB = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=name_DB,
        port=3306
    )
    cur = conn.cursor()  # on cree le curseur
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()  # on recupere les resultat
    #  (tous ce quon a demander avec le code SQL.)

    for row in rows:
        print(row)
    cur.close()
    conn.close()
