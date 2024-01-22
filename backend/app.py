from flask import Flask, jsonify, request, abort, make_response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

class Book:
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity

    def to_dict(self):
        return vars(self)

books = [
    Book("1", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 3),
    Book("2", "Harry Potter and the Chamber of Secrets", "J.K. Rowling", 4),
    Book("3", "Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", 5),
    Book("4", "Harry Potter and the Goblet of Fire", "J.K. Rowling", 6),
    Book("5", "Harry Potter and the Order of the Phoenix", "J.K. Rowling", 7),
    Book("6", "Harry Potter and the Half-Blood Prince", "J.K. Rowling", 8),
    Book("7", "Harry Potter and the Deathly Hallows", "J.K. Rowling", 9)
]

# Get all books
@app.route('/books', methods=['GET'])
@cross_origin()
def get_books():
    book_dicts = []
    for book in books:
        book_dict = book.to_dict()
        book_dicts.append(book_dict)
    return jsonify(book_dicts)

# Get a book by ID
@app.route('/books/<string:id>', methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.id == id:
            return jsonify(book.to_dict())
    abort(404, description="Book not found.")

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_id = str(len(books) + 1)  # Generate a unique ID
    new_book = Book(new_id, data['title'], data['author'], data['quantity'])
    books.append(new_book)
    return jsonify(new_book.to_dict()), 201

# Update a book by ID
@app.route('/books/<string:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    for book in books:
        if book.id == id:
            book.title = data['title']
            book.author = data['author']
            book.quantity = data['quantity']
            return jsonify(book.to_dict())
    abort(404, description="Book not found.")

# Delete a book by ID
@app.route('/books/<string:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book.id == id:
            books.remove(book)
            return make_response("", 204)
    abort(404, description="Book not found.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

