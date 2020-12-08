from sqlalchemy.orm import relationship
from base import session_factory
from publisher import Publisher
from author import Author
from book import Book

def print_books():
    for book in session.query(Book).order_by(Book.name):
        print(book)
        print("\t%s" % book.publisher)
        print("\t%s" % book.author)

if __name__ == '__main__':
    session = session_factory()
    Publisher.books = relationship("Book", order_by=Book.name, back_populates="publisher")
    Author.books = relationship("Book", order_by=Book.name, back_populates="author")
    print_books()