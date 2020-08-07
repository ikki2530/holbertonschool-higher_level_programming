#!/usr/bin/python3
"""COnnect to the database and executing a query"""
import MySQLdb
import sys


if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    
    cur.close()
    db_conn.close()
