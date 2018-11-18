from books.repositories import BookRepository
from books.domain import Book


class BookService:
    __book_repository: BookRepository

    def __init__(self, book_repository=BookRepository()):
        self.__book_repository = book_repository

    def get_all(self):
        books = self.__book_repository.get_all()
        return [book.to_dict() for book in books]

    def get_one(self, id):
        return self.__book_repository.get_one(id).to_dict()

    def get_by_isbn(self, isbn: int):
        return self.__book_repository.get_by_isbn(isbn).to_dict()

    def add(self, book_json):
        new_book = Book(isbn=book_json['isbn'], name=book_json['name'], price=book_json['price'])
        return self.__book_repository.add(new_book)

    def update(self, id, book_json):
        updated_book = Book(id=id, isbn=book_json['isbn'], name=book_json['name'], price=book_json['price'])
        self.__book_repository.update(updated_book)

    def patch(self, id, patch_payload):
        book = self.__book_repository.get_one(id)
        for field, value in patch_payload.items():
            setattr(book, field, value)
        self.__book_repository.update(book)

    def delete(self, isbn):
        self.__book_repository.delete(isbn)
