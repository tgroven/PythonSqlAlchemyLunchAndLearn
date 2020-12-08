from sqlalchemy import Column, Integer, String, SmallInteger
from base import Base

class Author(Base):
    __tablename__ = 'author'

    author_id = Column('authorid', Integer, primary_key=True)
    first_name = Column('firstname', String)
    last_name = Column('lastname', String)
    rating = Column(SmallInteger)

    def __repr__(self):
        return "<Author(name='%s %s', rating='%s')>" % (self.first_name, self.last_name, self.rating)
