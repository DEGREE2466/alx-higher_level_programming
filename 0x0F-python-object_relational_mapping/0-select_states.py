#!/usr/bin/python3
"""
Lists all states from the hbtn_0e_0_usa database
"""


def main():
    """
    List 'states' table of the database 'hbtn_0e_0_usa' in an ascending
    order by id's
    """
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
