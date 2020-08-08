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
    nam = sys.argv[4]
    db_conn = MySQLdb.connect(host=lh, user=u, passwd=p, db=d, port=3306)

    cur = db_conn.cursor()
    q = """SELECT * FROM states WHERE name LIKE BINARY '{}'
    ORDER BY states.id""".format(nam)
    cur.execute(q)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db_conn.close()
