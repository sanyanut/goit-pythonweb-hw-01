from abc import ABC, abstractmethod
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year


class LibraryReadInterface(ABC):
    @abstractmethod
    def show_books(self) -> None:
        pass


class LibraryWriteInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass


class LibraryInterface(LibraryReadInterface, LibraryWriteInterface, ABC):
    pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        for book_item in self.books:
            if book.title == book_item.title:
                logging.info("Book with the same title already exists.")
                return

        self.books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return

        logging.info("Book not found.")

    def show_books(self) -> None:
        if len(self.books) == 0:
            logging.info("No books in library.")
            return

        for book in self.books:
            logging.info(
                f"Title: {book.title}, Author: {book.author}, Year: {book.year}"
            )


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
