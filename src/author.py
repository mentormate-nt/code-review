import csv

from utils import get_db_connection

class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class authorSeeder:
    def __init__(self):
        self.conn = get_db_connection()
        self.query = '''INSERT INTO author (first_name, last_name) VALUES("{}", "{}")'''

    def instantiate_data(self, array_data):
        for data in array_data:
            author = Author(data['first_name'], data['last_name'])
            self.insert(author)

    def insert(self, obj):
        c = self.conn.cursor()
        c.execute(self.query.format(obj.first_name, obj.last_name))

        self.conn.commit()

class authorCvsSeeder:
    def __init__(self):
        self.conn = get_db_connection()
        self.query = '''INSERT INTO author (first_name, last_name) VALUES("{}", "{}")'''

    def read_file(self, file):
        inputFile = csv.DictReader(open(file))

        array_data = [row for row in inputFile]
        self.instantiate_data(array_data)
        


    def instantiate_data(self, array_data):
        for data in array_data:
            author = Author(data['first_name'], data['last_name'])
            self.insert(author)

    def insert(self, obj):
        c = self.conn.cursor()
        c.execute(self.query.format(obj.first_name, obj.last_name))

        self.conn.commit()

