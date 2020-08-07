#!/usr/bin/python3
"""COnnect to the database and executing a query"""
import MySQLdb
import sys


if __name__ == "__main__":
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db_conn = MySQLdb.connect(host=lh, user=u, passwd=p, db=d, port=3306)

    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY states.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db_conn.close()
