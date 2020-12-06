from sqlalchemy import Column, Integer, String, Boolean, DateTime, LargeBinary, Numeric, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from customeraddress import CustomerAddress
from address import Address
from base import Base


class SalesOrderDetail(Base):
    __tablename__ = 'salesorderdetail'
    __table_args__ = {'schema': 'SalesLT'}

    sales_order_detail_id = Column('SalesOrderDetailID', Integer, primary_key=True)
    sales_order_id = Column('SalesOrderID', Integer)
    order_quantity = Column('OrderQty', SmallInteger)
    product_id = Column('ProductID', Integer)
    unit_price = Column('UnitPrice', Numeric(10, 2))
    unit_price_discount = Column('UnitPriceDiscount', Numeric(10, 2))
    modified_date = Column('ModifiedDate', DateTime)
