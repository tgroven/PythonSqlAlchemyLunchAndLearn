from decimal import Decimal
from sqlalchemy import create_engine


def create_db_engine():
    return create_engine(
        "mssql+pyodbc://python:python@localhost/AdventureWorksLT2019?driver=ODBC+Driver+17+for+SQL+Server")


def get_customer_details(company_name):
    customer_result = connection.execute("SELECT * FROM SalesLT.Customer WHERE CompanyName = '" + company_name +
                                            "' ORDER BY CustomerID DESC")

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
    address_result = connection.execute(
        "SELECT * FROM SalesLT.CustomerAddress WHERE CustomerId = " + str(customer_id) +
        " AND AddressType = 'Main Office'")

    if address_result.returns_rows:
        row = address_result.first()

        if row is None:
            print("Address not found.")
            return None

        print("Customer Address ID is: " + str(row['AddressID']) + " and Address Type is " + row['AddressType'])
        address = {'AddressID': row['AddressID'], 'AddressType': row['AddressType']}

        return address


def get_product_details(product_name):
    product_result = connection.execute(
        "SELECT * FROM SalesLT.Product WHERE Name = '" + product_name + "'")

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

    connection.execute(
        "INSERT INTO SalesLT.SalesOrderHeader (RevisionNumber, OrderDate, DueDate, Status, OnlineOrderFlag, " +
        "CustomerID, ShipToAddressID, BillToAddressID, ShipMethod, SubTotal, TaxAmt, Freight, ModifiedDate) " +
        "VALUES (2, SYSDATETIME(), SYSDATETIME(), 5, 0, " + str(customer_details['CustomerID']) + ", " +
        str(address_details['AddressID']) + ", " + str(address_details['AddressID']) + ", 'CARGO TRANSPORT 5', " +
        str(sub_total) + ", " + str(tax_amount) + ", " + str(freight) + ", SYSDATETIME())")

    order_header_result = connection.execute("SELECT SCOPE_IDENTITY()")

    if order_header_result.returns_rows:
        row = order_header_result.first()

        if row is None:
            print("Sales Order Header ID not found.")
            return None

        print("Sales Order Header ID is: " + str(row[0]))
        sales_order_header = {'SalesOrderHeaderID': row[0], 'SubTotal': sub_total,
                              'TaxAmount': tax_amount, 'Freight': freight}

        return sales_order_header


def create_sales_order_detail():
    connection.execute(
        "INSERT INTO SalesLT.SalesOrderDetail (SalesOrderID, OrderQty, ProductID, UnitPrice, UnitPriceDiscount, " +
        "ModifiedDate) " +
        "VALUES (" + str(sales_order_header_details['SalesOrderHeaderID']) + ", 1, " +
        str(product_details['ProductID']) + ", " + str(product_details['ListPrice']) + ", 0, SYSDATETIME())")

    order_detail_result = connection.execute("SELECT SCOPE_IDENTITY()")

    if order_detail_result.returns_rows:
        row = order_detail_result.first()

        if row is None:
            print("Sales Order Detail ID not found.")
            return None

        print("Sales Order Detail ID is: " + str(row[0]))
        sales_order_detail = {'SalesOrderDetailID': row[0]}

        return sales_order_detail


if __name__ == '__main__':
    engine = create_db_engine()

    with engine.connect() as connection:
        customer_details = get_customer_details('Sundry Sporting Goods')
        address_details = get_customer_address_details(customer_details['CustomerID'])
        product_details = get_product_details('HL Mountain Pedal')

        sales_order_header_details = create_sales_order_header()
        sales_order_detail_details = create_sales_order_detail()
