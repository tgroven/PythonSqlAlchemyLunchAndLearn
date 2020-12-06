from sqlalchemy import Column, Integer, String, Boolean, DateTime, LargeBinary, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from customeraddress import CustomerAddress
from address import Address
from base import Base


class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'SalesLT'}

    product_id = Column('ProductID', Integer, primary_key=True)
    name = Column(String(50))
    product_number = Column('ProductNumber', String(25))
    color = Column(String(15))
    standard_cost = Column('StandardCost', Numeric(10, 2))
    list_price = Column('ListPrice', Numeric(10, 2))
    size = Column(String(5))
    weight = Column(Numeric(8, 2))
    product_category_id = Column('ProductCategoryID', Integer, ForeignKey('ProductCategory.ProductCategoryID'))
    product_model_id = Column('ProductModelID', Integer, ForeignKey('ProductModel.ProductModelID'))
    sell_start_date = Column('SellStartDate', DateTime)
    sell_end_date = Column('SellEndDate', DateTime)
    discontinued_date = Column('DiscontinuedDate', DateTime)
    thumbnail_photo = Column('ThumbNailPhoto', LargeBinary("max"))
    thumbnail_photo_filename = Column('ThumbnailPhotoFileName', String(50))
    rowguid = Column(UNIQUEIDENTIFIER)
    modified_date = Column('ModifiedDate', DateTime)
