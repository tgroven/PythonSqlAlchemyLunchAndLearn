from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from customeraddress import CustomerAddress
from address import Address
from base import Base


class Customer(Base):
    __tablename__ = 'customer'
    __table_args__ = {'schema': 'SalesLT'}

    customer_id = Column('CustomerID', Integer, primary_key=True)
    namestyle = Column(Boolean)
    title = Column(String(8))
    first_name = Column('FirstName', String(50))
    middle_name = Column('MiddleName', String(50))
    last_name = Column('LastName', String(50))
    suffix = Column(String(10))
    company_name = Column('CompanyName', String(128))
    sales_person = Column('SalesPerson', String(256))
    email_address = Column('EmailAddress', String(50))
    phone = Column(String(25))
    password_hash = Column('PasswordHash', String(128))
    password_salt = Column('PasswordSalt', String(10))
    rowguid = Column(UNIQUEIDENTIFIER)
    modified_date = Column('ModifiedDate', DateTime)