#!/usr/bin/python3
"""
Lists all states from the hbtn_0e_0_usa database
"""


def main():
    """
    List 'states' table of 'hbtn_0e_0_usa' database in ascending
    order by id's
    """
    import MySQLdb
    from sys import argv

    usr = str(argv[1])
    pasw = str(argv[2])
    db_name = str(argv[3])

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=usr, passwd=pasw, db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id;")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
