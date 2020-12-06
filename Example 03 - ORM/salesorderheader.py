from sqlalchemy import Column, Integer, String, Boolean, DateTime, LargeBinary, Numeric, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from customeraddress import CustomerAddress
from address import Address
from base import Base


class SalesOrderHeader(Base):
    __tablename__ = 'salesorderheader'
    __table_args__ = {'schema': 'SalesLT'}

    sales_order_id = Column('SalesOrderID', Integer, primary_key=True)
    revision_number = Column('RevisionNumber', SmallInteger)
    order_date = Column('OrderDate', DateTime)
    due_date = Column('DueDate', DateTime)
    ship_date = Column('ShipDate', DateTime)
    status = Column(SmallInteger)
    online_order_flag = Column('OnlineOrderFlag', Boolean)
    #sales_order_number = Column('SalesOrderNumber', String(25))
    purchase_order_number = Column('PurchaseOrderNumber', String(25))
    account_number = Column('AccountNumber', String(15))
    customer_id = Column('CustomerID', Integer)#, ForeignKey('Customer.CustomerID'))
    ship_to_address_id = Column('ShipToAddressID', Integer)#, ForeignKey('address.address_id'))
    bill_to_address_id = Column('BillToAddressID', Integer)#, ForeignKey('address.address_id'))
    ship_method = Column('ShipMethod', String(50))
    credit_card_approval_code = Column('CreditCardApprovalCode', String(15))
    sub_total = Column('SubTotal', Numeric(10, 2))
    tax_amount = Column('TaxAmt', Numeric(10, 2))
    freight = Column(Numeric(10, 2))
    #total_due = Column('TotalDue', Numeric(10, 2))
    comment = Column(String("max"))
    #rowguid = Column(UNIQUEIDENTIFIER)
    modified_date = Column('ModifiedDate', DateTime)
