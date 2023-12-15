#!/usr/bin/python3
""""""
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
        "SELECT cities.name FROM cities WHERE cities.state_id = (",
        "SELECT states.id FROM states WHERE states.name=%(name)s)",
        "GROUP BY cities.id"
    ])
    cur.execute(qr, {'name': sys.argv[4]})
    rows = cur.fetchall()
    print(', '.join([i[0] for i in rows]))
    cur.close()
    db.close()
