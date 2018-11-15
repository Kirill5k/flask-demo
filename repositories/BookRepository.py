from domain.Book import Book


class BookRepository:
    __current_isbn_index = 4
    __books = {
        1: Book(1, 'Book 1', 9.99),
        2: Book(2, 'Book 2', 19.99),
        3: Book(3, 'Book 3', 29.99)
    }

    def get_all(self):
        return list(self.__books.values())

    def get_one(self, isbn: int):
        if isbn not in self.__books:
            raise ValueError('not found')
        return self.__books.get(isbn)

    def add(self, new_book: Book):
        new_book.isbn = self.__current_isbn_index
        self.__books[new_book.isbn] = new_book
        self.__current_isbn_index += 1
        return new_book.isbn

    def update(self, updated_book: Book):
        if updated_book.isbn not in self.__books:
            raise ValueError('not found')
        self.__books[updated_book.isbn] = updated_book

    def delete(self, isbn: int):
        if isbn not in self.__books:
            raise ValueError('not found')
        del self.__books[isbn]
