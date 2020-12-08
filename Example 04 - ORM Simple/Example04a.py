from sqlalchemy.orm import relationship
from base import session_factory
from publisher import Publisher
from author import Author
from book import Book

def print_publishers():
    for publisher in session.query(Publisher).order_by(Publisher.name):
        print(publisher)
        for book in publisher.books:
            print("\t%s" % book)
            print("\t\t%s" % book.author)

if __name__ == '__main__':
    session = session_factory()
    Publisher.books = relationship("Book", order_by=Book.name, back_populates="publisher")
    Author.books = relationship("Book", order_by=Book.name, back_populates="author")
    print_publishers()