#!/usr/bin/python3
"""
takes in arguments and displays all values in the states 
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
takes 4 arguments: mysql username, mysql password, database
name and state name searched (safe from MySQL injection)
"""

import sys
import MySQLdb


def safe_filter():
    """ defining func """

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
    cur.close()
    conn.close()


if __name__ == '__main__':
    safe_filter()
