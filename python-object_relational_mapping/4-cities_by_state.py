#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa` along with their
corresponding state names. The results are sorted by the city ID in ascending
order.
Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The username to connect to the MySQL server.
    mysql_password: The password to connect to the MySQL server.
    database_name: The name of the database to query (`hbtn_0e_4_usa`).

Requirements:
    - Only the MySQLdb module is allowed.
    - The script connects to a MySQL server running on localhost at port 3306.
    - The script must use only one call to the execute() method.
    - Must not execute code when imported as a module.

Output:
    Prints each city’s ID, name, and corresponding state name as a tuple:
    (city_id, city_name, state_name)
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
