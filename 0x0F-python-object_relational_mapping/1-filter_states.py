#!/usr/bin/python3
"""This script lists all states starting with N
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    qr = " ".join([
        "SELECT * FROM states",
        "WHERE states.name LIKE BINARY 'N%'",
        "ORDER BY states.id"
    ])
    cur.execute(qr)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
