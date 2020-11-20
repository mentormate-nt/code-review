import collections

import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db_connection():
    con = sqlite3.connect('library.db', check_same_thread=False)
    con.row_factory = dict_factory
    return con