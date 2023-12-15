#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    try:
        cur.execute("SLECT * FROM states WHERE states.name LIKE "N%" ORDER BY states.id")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        try:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: %s" % str(e))
    for row in rows:
        print(row)
    cur.close()
