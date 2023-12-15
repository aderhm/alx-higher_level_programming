#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa
where name matches the argument, considering SQL Injection.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        prot=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    qr = " ".join([
        "SELECT * FROM states",
        "WHERE states.name LIKE BINARY %s",
        "ORDER BY states.id"
    ])
    cur.exercute(qr, (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
