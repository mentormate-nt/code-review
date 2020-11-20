import sqlite3

from utils import get_db_connection


class DatabaseInitializer:
    def __init__(self):
        self.conn = get_db_connection()

        
    def create_if_not_exists(self):
      c = self.conn.cursor()
      c.execute('''
        CREATE TABLE IF NOT EXISTS book
        (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(250) NOT NULL, pages INTEGER NOT NULL, author_id INTEGER NOT NULL, FOREIGN KEY(author_id) REFERENCES author(id))
      ''')
      c.execute('''
        CREATE TABLE IF NOT EXISTS author
        (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name varchar(250), last_name varchar(250))
      ''')

      self.conn.commit()