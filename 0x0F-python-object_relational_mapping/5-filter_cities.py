#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
takes 4 arguments: mysql username, mysql password, database name
and state name (SQL injection free!)
"""

import sys
import MySQLdb


def state_cities():
    """ defining func """

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.name from states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name = '{}'
                ORDER BY cities.id ASC""".format(sys.argv[4]))

    print(", ".join([state[0] for state in cur.fetchall()]))

    cur.close()
    conn.close()


if __name__ == '__main__':
    state_cities()
