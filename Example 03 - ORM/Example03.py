import datetime
from decimal import Decimal
from sqlalchemy import MetaData, select, desc
from customer import Customer
from customeraddress import CustomerAddress
from address import Address
from product import Product
from salesorderheader import SalesOrderHeader
from salesorderdetail import SalesOrderDetail
from base import session_factory
from sqlalchemy.orm import relationship


def get_customer_address(company_name):
    for customer, customeraddress, address in session.query(Customer, CustomerAddress, Address)\
            .filter(Customer.company_name == company_name, CustomerAddress.customer_id == Customer.customer_id,
                    Address.address_id == CustomerAddress.address_id):
        print(company_name + " Customer ID is: " + str(customer.customer_id) + " and Address ID is " +
              str(address.address_id))

        return customer, address


def get_product(product_name):
    for product in session.query(Product).filter(Product.name == product_name):
        print("Product ID: " + str(product.product_id))

        return product


def create_sales_order_header():
     sub_total = product.list_price * 1
     tax_amount = product.list_price * Decimal('0.075')
     freight = 20

     sales_order_header = SalesOrderHeader(revision_number=2, order_date=datetime.datetime.now(),
                                           due_date=datetime.datetime.now(), status=5,
                                           online_order_flag=0, customer_id=customer.customer_id,
                                           ship_to_address_id=address.address_id,
                                           bill_to_address_id=address.address_id,
                                           ship_method="CARGO TRANSPORT 5", sub_total=sub_total,
                                           tax_amount=tax_amount, freight=freight,
                                           modified_date=datetime.datetime.now())

     session.add(sales_order_header)

     print(str(sales_order_header.sales_order_id))
     print(session.new)

     session.commit()
     print(str(sales_order_header.sales_order_id))

     return sales_order_header


def create_sales_order_detail():
    sales_order_detail = SalesOrderDetail(sales_order_id=sales_order_header.sales_order_id,
                                          order_quantity=1, product_id=product.product_id,
                                          unit_price=product.list_price, unit_price_discount=0,
                                          modified_date=datetime.datetime.now())

    session.add(sales_order_detail)

    print(str(sales_order_detail.sales_order_detail_id))
    print(session.new)

    session.commit()
    print(str(sales_order_detail.sales_order_detail_id))

    return sales_order_detail


if __name__ == '__main__':
    session = session_factory()
    customer, address = get_customer_address('Sundry Sporting Goods')
    product = get_product('HL Mountain Pedal')

    sales_order_header = create_sales_order_header()
    sales_order_detail = create_sales_order_detail()
