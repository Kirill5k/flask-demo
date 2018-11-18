from books.domain import Book, db
from sqlalchemy.exc import IntegrityError


class BookRepository:
    def get_all(self):
        return Book.query.all()

    def get_one(self, id):
        book = Book.query.get(id)
        if not book:
            raise ValueError('not found')
        return book

    def get_by_isbn(self, isbn: int):
        book = Book.query.filter_by(isbn=isbn).first()
        if not book:
            raise ValueError('not found')
        return book

    def add(self, new_book: Book):
        try:
            db.session.add(new_book)
            db.session.commit()
            return new_book.id
        except IntegrityError as error:
            raise ValueError(', '.join(error.orig.args))

    def update(self, updated_book: Book):
        try:
            db.session.add(updated_book)
            db.session.commit()
        except IntegrityError as error:
            raise ValueError(', '.join(error.orig.args))

    def delete(self, id: int):
        book = self.get_one(id)
        db.session.delete(book)
        db.session.commit()
