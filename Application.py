from flask import flask
app = Flask__(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(50), unique = True, nullable = False)
    publisher = db.Column(db.String(50), unique = True)
    
    def__repr__(self):
        return f"{self.name} - {self.name,author,publisher}"
    
     @app.route('/')
    def index():
        return'Hello!'
    
    @app.route ("/books/<id>")
def get_books():
    books = Book.query.all()
    
    output = []
    for books in books: 
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)
        
     return {"books": output}

@app.route ('/books', methods = ['POST'])
def add_book():
    book = Book(book_name = request.json['book name'], author = request.json['author'], publisher = request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route ('/books', methods = ['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "book is not found"}
   db.session.delete(book)
    db.session.commit()
        return {"message": "yeet!"}
    
