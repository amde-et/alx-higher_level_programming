#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:
takes 3 arguments: mysql username, mysql password and database name (no argument validation needed)
"""

import sys
import MySQLdb


def list_state():
    """  lists all states from the database hbtn_0e_0_usa"""

    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_state()


