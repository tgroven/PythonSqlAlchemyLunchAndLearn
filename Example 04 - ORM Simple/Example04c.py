from sqlalchemy.orm import relationship
from base import session_factory
from publisher import Publisher
from author import Author
from book import Book

def print_authors():
    for author in session.query(Author).order_by(Author.last_name):
        print(author)
        for book in author.books:
            print("\t%s" % book)
            print("\t%s" % book.publisher)

if __name__ == '__main__':
    session = session_factory()
    Publisher.books = relationship("Book", order_by=Book.name, back_populates="publisher")
    Author.books = relationship("Book", order_by=Book.name, back_populates="author")
    print_authors()