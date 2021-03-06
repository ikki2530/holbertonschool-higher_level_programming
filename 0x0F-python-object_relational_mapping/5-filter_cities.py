#!/usr/bin/python3
"""COnnect to the database and executing a query"""


import MySQLdb
import sys


if __name__ == "__main__":
    """COnnect to the database and executing a query"""
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    state = sys.argv[4]
    db_conn = MySQLdb.connect(host=lh, user=u, passwd=p, db=d, port=3306)

    cur = db_conn.cursor()

    cur.execute(("""SELECT cities.name FROM cities
    JOIN states ON (states.id = cities.state_id) WHERE states.name=%s
    ORDER BY cities.id"""), (state,))

    rows = cur.fetchall()
    if rows:
        lg = len(rows)
        for i in range(lg):
            if i == lg - 1:
                print(rows[i][0])
            else:
                print(rows[i][0], end=", ")
    else:
        print()
    cur.close()
    db_conn.close()
