import datetime
from decimal import Decimal
from sqlalchemy import create_engine, MetaData, select, desc


def create_db_engine():
    return create_engine(
        "mssql+pyodbc://python:python@localhost/AdventureWorksLT2019?driver=ODBC+Driver+17+for+SQL+Server")


def get_customer_details(company_name):
    customers_table = metadata.tables['SalesLT.Customer']
    select_statement = select([customers_table.c.CustomerID, customers_table.c.EmailAddress])\
        .where(customers_table.c.CompanyName == company_name)\
        .order_by(customers_table.c.CustomerID.desc())

    customer_result = connection.execute(select_statement)

    if customer_result.returns_rows:
        row = customer_result.first()

        if row is None:
            print(company_name + " not found.")
            return None

        print(company_name + " Customer ID is: " + str(row['CustomerID']) + " and EmailAddress is " +
              row['EmailAddress'])
        customer = {'CustomerID': row['CustomerID'], 'EmailAddress': row['EmailAddress']}

        return customer


def get_customer_address_details(customer_id):
    customer_addresses_table = metadata.tables['SalesLT.CustomerAddress']
    select_statement = select([customer_addresses_table]).where(customer_addresses_table.c.CustomerID == customer_id)\
        .where(customer_addresses_table.c.AddressType == 'Main Office')\
        .order_by(desc(customer_addresses_table.c.CustomerID))

    address_result = connection.execute(select_statement)

    if address_result.returns_rows:
        row = address_result.first()

        if row is None:
            print("Address not found.")
            return None

        print("Customer Address ID is: " + str(row['AddressID']) + " and Address Type is " + row['AddressType'])
        address = {'AddressID': row['AddressID'], 'AddressType': row['AddressType']}

        return address


def get_product_details(product_name):
    products_table = metadata.tables['SalesLT.Product']
    select_statement = select([products_table]).where(products_table.c.Name == product_name)

    product_result = connection.execute(select_statement)

    if product_result.returns_rows:
        row = product_result.first()

        if row is None:
            print("Product not found.")
            return None

        print("Product ID is: " + str(row['ProductID']) + " and List Price is " + str(row['ListPrice']) +
              " and Weight is " + str(row['Weight']))
        product = {'ProductID': row['ProductID'], 'ListPrice': row['ListPrice'], 'Weight': row['Weight']}

        return product


def create_sales_order_header():
    sub_total = product_details['ListPrice'] * 1
    tax_amount = product_details['ListPrice'] * Decimal('0.075')
    freight = 20

    sales_order_headers_table = metadata.tables['SalesLT.SalesOrderHeader']
    order_header_result = connection.execute(sales_order_headers_table.insert(),
                                             {'RevisionNumber': 2, 'OrderDate': datetime.datetime.now(),
                                              'DueDate': datetime.datetime.now(), 'Status': 5,
                                              'OnlineOrderFlag': 0, 'CustomerID': customer_details['CustomerID'],
                                              'ShipToAddressID': address_details['AddressID'],
                                              'BillToAddressID': address_details['AddressID'],
                                              'ShipMethod': 'CARGO TRANSPORT 5', 'SubTotal': sub_total,
                                              'TaxAmt': tax_amount, 'Freight': freight,
                                              'ModifiedDate': datetime.datetime.now()})

    if order_header_result.is_insert:
        print("Sales Order Header ID is: " + str(order_header_result.inserted_primary_key[0]))
        sales_order_header = {'SalesOrderHeaderID': order_header_result.inserted_primary_key[0], 'SubTotal': sub_total,
                              'TaxAmount': tax_amount, 'Freight': freight}

        return sales_order_header


def create_sales_order_detail():
    sales_order_details_table = metadata.tables['SalesLT.SalesOrderDetail']
    order_detail_result = connection.execute(sales_order_details_table.insert(None, False),
                                             {'SalesOrderID': sales_order_header_details['SalesOrderHeaderID'],
                                              'OrderQty': 1, 'ProductID': product_details['ProductID'],
                                              'UnitPrice': product_details['ListPrice'], 'UnitPriceDiscount': 0,
                                              'ModifiedDate': datetime.datetime.now()})

    if order_detail_result.is_insert:
        print("Sales Order Detail ID is: " + str(order_detail_result.inserted_primary_key[0]))
        sales_order_detail = {'SalesOrderDetailID': order_detail_result.inserted_primary_key[0]}

        return sales_order_detail


def get_sales_order_details(sales_order_id):
    sales_order_header_table = metadata.tables['SalesLT.SalesOrderHeader']
    sales_order_detail_table = metadata.tables['SalesLT.SalesOrderDetail']
    select_statement = select([sales_order_header_table, sales_order_detail_table])\
        .where(sales_order_header_table.c.SalesOrderID == sales_order_detail_table.c.SalesOrderID)\
        .where(sales_order_header_table.c.SalesOrderID == sales_order_id)

    query_result = connection.execute(select_statement)

    for row in query_result:
        print(row)


def get_sales_order_details_manual_join(sales_order_id):
    sales_order_header_table = metadata.tables['SalesLT.SalesOrderHeader']
    sales_order_detail_table = metadata.tables['SalesLT.SalesOrderDetail']
    select_statement = select([sales_order_header_table.c.SalesOrderNumber,
                               sales_order_header_table.c.DueDate])\
        .select_from(
            sales_order_header_table.join(sales_order_detail_table,
                                          sales_order_detail_table.c.SalesOrderID == sales_order_header_table.c.SalesOrderID))\
        .where(sales_order_header_table.c.SalesOrderID == sales_order_id)

    query_result = connection.execute(select_statement)

    for row in query_result:
        print(row)


if __name__ == '__main__':
    engine = create_db_engine()
    metadata = MetaData(schema='SalesLT', bind=engine)
    metadata.reflect()

    with engine.connect() as connection:
        customer_details = get_customer_details('Sundry Sporting Goods')
        address_details = get_customer_address_details(customer_details['CustomerID'])
        product_details = get_product_details('HL Mountain Pedal')

        sales_order_header_details = create_sales_order_header()
        sales_order_detail_details = create_sales_order_detail()

        get_sales_order_details(sales_order_header_details['SalesOrderHeaderID'])
        get_sales_order_details_manual_join(sales_order_header_details['SalesOrderHeaderID'])
