from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from publisher import Publisher
from base import Base

class Book(Base):
    __tablename__ = 'book'

    book_id = Column('bookid', Integer, primary_key=True)
    publisher_id = Column('publisherid', Integer, ForeignKey('publisher.publisherid'))
    author_id = Column('authorid', Integer, ForeignKey('author.authorid'))
    name = Column(String)
    rating = Column(SmallInteger)

    publisher = relationship("Publisher", back_populates="books")
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return "<Book(name='%s', rating='%s')>" % (self.name, self.rating)
