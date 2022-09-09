#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
take 3 arguments: mysql username, mysql password and database name
"""

import sys
import MySQLdb


def lst_cities():
    """ defining func """

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name 
         FROM states 
         INNER JOIN cities ON states.id = cities.state_id 
         ORDER BY cities.id ASC""")
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()


if __name__ == '__main__':
    lst_cities()
