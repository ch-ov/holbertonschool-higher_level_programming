#!/usr/bin/python3
"""takes the name of a state as argument and lists all cities of that state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    pycode = """SELECT cities.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name LIKE %s
                ORDER BY cities.id ASC"""
    cur.execute(pycode, (argv[4], ))
    print(', '.join([f"{row[0]}" for row in cur.fetchall()]))
    cur.close()
    db.close()
