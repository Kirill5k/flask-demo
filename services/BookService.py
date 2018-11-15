from dataclasses import asdict
from repositories.BookRepository import BookRepository
from domain.Book import Book


class BookService:
    __book_repository: BookRepository

    def __init__(self, book_repository=BookRepository()):
        self.__book_repository = book_repository

    def get_all(self):
        books = self.__book_repository.get_all()
        return [asdict(book) for book in books]

    def get_one(self, isbn: int):
        return self.__book_repository.get_one(isbn)

    def add(self, new_book_json):
        new_book = Book(None, new_book_json['name'], new_book_json['price'])
        return self.__book_repository.add(new_book)

    def update(self, isbn, updated_book_json):
        updated_book = Book(isbn, updated_book_json['name'], updated_book_json['price'])
        self.__book_repository.update(updated_book)

    def patch(self, isbn, patch_payload):
        book = self.__book_repository.get_one(isbn)
        for field, value in patch_payload.items():
            setattr(book, field, value)
        self.__book_repository.update(book)

    def delete(self, isbn):
        self.__book_repository.delete(isbn)
