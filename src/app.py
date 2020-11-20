from flask import Flask, request, jsonify
from base import DatabaseInitializer
from utils import get_db_connection

from book import bookSeeder, bookCvsSeeder
from author import authorSeeder, authorCvsSeeder



app = Flask(__name__)

conn = get_db_connection()

@app.route('/book', methods=['POST'])
def create():
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO book (title, pages, author_id) VALUES("{}", "{}", "{}")'''.format(data['title'], data['pages'], data['author']))
    conn.commit()

    return {'title': data['title'], 'pages': data['pages'], 'author': data['author']}

@app.route('/book/<int:book_id>')
def read(bookId):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM book WHERE id={}'''.format(bookId))

    result = cursor.fetchone()
    return result

@app.route('/book/<int:book_id>', methods=['PUT'])
def update(bookId):
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('''UPDATE book SET title="{}", pages={}, author_id={} WHERE id={}'''.format(data['title'], data['pages'], data['author'], bookId))

    conn.commit()
    return data

@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete(bookId):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM book WHERE id={}'''.format(bookId))

    conn.commit()
    return 'Book with id of {} was removed.'.format(bookId)


@app.route('/author/<int:authod_id>/books')
def search_books(authodId):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM book''')
    books = cursor.fetchall()
    '''
    Getting all the books by author_id
    '''
    result = list(filter(lambda d: d['author_id'] == authodId, books))
    return jsonify(result)


@app.route('/author', methods=['POST'])
def createAuthor():
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO author (first_name, last_name) VALUES("{}", "{}")'''.format(data['first_name'], data['last_name']))
    conn.commit()

    return {'first_name': data['first_name'], 'last_name': data['last_name']}

@app.route('/author/<int:author_id>', methods=['GET'])
def getAuthor(author_id):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM author WHERE id={}'''.format(author_id))

    result = cursor.fetchone()
    return result

@app.route('/author/<int:author_id>', methods=['PUT'])
def updateAuthor(author_id):
    data = request.get_json()
    cursor = conn.cursor()
    cursor.execute('''UPDATE author SET first_name="{}", last_name="{}" WHERE id={}'''.format(data['first_name'], data['last_name'], author_id))

    conn.commit()
    return data


@app.route('/author/<int:author_id>', methods=['DELETE'])
def deleteAuthor(author_id):
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM author WHERE id={}'''.format(author_id))

    conn.commit()
    return 'Author with id of {} was removed.'.format(author_id)


if __name__ == "__main__":
    dict_authors = [
        {'first_name': 'Harry', 'last_name': 'Potter'},
        {"first_name": "Lord Rings", "last_name": 'Rings'},
        {"first_name": "Game", "last_name": 'Thrones'}
    ]

    dict_books = [
        {'title': 'Harry Potter', 'pages': 1000, 'author': 0},
        {"title": "Lord of the Rings", "pages": 2000, "author": 1},
        {"title": "Game of Thrones", "pages": 3000, "author": 2}
    ]

    db = DatabaseInitializer()
    db.create_if_not_exists()

    book_seeder = bookSeeder()
    book_seeder.instantiate_data(dict_books)

    book_cvs_seeder = bookCvsSeeder()
    book_cvs_seeder.read_file('myFile1.csv')

    author_seeder = authorSeeder()
    author_seeder.instantiate_data(dict_authors)

    author_cvs_seeder = authorCvsSeeder()
    author_cvs_seeder.read_file('myFile0.csv')

    app.run()

