import csv

from utils import get_db_connection


class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author
    
class bookSeeder:

    def __init__(self):
        self.conn = get_db_connection()
        self.query = '''INSERT INTO book (title, pages, author_id) VALUES("{}", "{}", "{}")'''

    def instantiate_data(self, array_data):
        for data in array_data:
            book = Book(data['title'], data['pages'], data['author'])
            self.insert(book)

    def insert(self, obj):
        c = self.conn.cursor()
        c.execute(self.query.format(obj.title, obj.pages, obj.author))

        self.conn.commit()



class bookCvsSeeder:
    def __init__(self):
        self.conn = get_db_connection()
        self.query = '''INSERT INTO book (title, pages, author_id) VALUES("{}", "{}", "{}")'''

    def read_file(self, file):
        inputFile = csv.DictReader(open(file))

        array_data = [row for row in inputFile]
        self.instantiate_data(array_data)
        
    def instantiate_data(self, array_data):
        for data in array_data:
            book = Book(data['title'], data['pages'], data['author'])
            self.insert(book)

    def insert(self, obj):
        c = self.conn.cursor()
        c.execute(self.query.format(obj.title, obj.pages, obj.author))

        self.conn.commit()



