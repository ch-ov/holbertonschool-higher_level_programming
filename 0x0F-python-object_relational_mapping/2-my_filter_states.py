#!/usr/bin/python3
"""displays values in states table of hbtn_0e_0_usa where name == argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    pycode = """SELECT *
                FROM states
                WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cur.execute(pycode)
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
