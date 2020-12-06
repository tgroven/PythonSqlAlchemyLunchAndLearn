from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from base import Base


class CustomerAddress(Base):
    __tablename__ = 'customeraddress'
    __table_args__ = {'schema': 'SalesLT'}

    customer_id = Column('CustomerID', Integer, ForeignKey('Customer.CustomerID'), primary_key=True)
    address_id = Column('AddressID', Integer, ForeignKey('Address.AddressID'), primary_key=True)
    address_type = Column('AddressType', String(50))
    rowguid = Column(UNIQUEIDENTIFIER)
    modified_date = Column('ModifiedDate', DateTime)


