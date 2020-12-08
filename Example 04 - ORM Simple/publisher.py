from sqlalchemy import Column, Integer, String
from base import Base

class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id = Column('publisherid', Integer, primary_key=True)
    name = Column(String)
    website = Column(String)

    def __repr__(self):
        return "<Publisher(name='%s', website='%s')>" % (self.name, self.website)
