#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
takes 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
"""

import sys
import MySQLdb


def state():
    """ defining func"""

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name FROM `states` where `name` LIKE '{}' ORDER BY id ASC".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()


if __name__ == '__main__':
    state()
