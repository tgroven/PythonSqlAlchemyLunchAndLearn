from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
#from customer import Customer
from base import Base


class Address(Base):
    __tablename__ = 'address'
    __table_args__ = {'schema': 'SalesLT'}

    address_id = Column('AddressID', Integer, primary_key=True)
    address_line_1 = Column('AddressLine1', String(60))
    address_line_2 = Column('AddressLine2', String(60))
    city = Column(String(30))
    state_province = Column('StateProvince', String(50))
    country_region = Column('CountryRegion', String(50))
    postal_code = Column('PostalCode', String(15))
    rowguid = Column(UNIQUEIDENTIFIER)
    modified_date = Column('ModifiedDate', DateTime)
