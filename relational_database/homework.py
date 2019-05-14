def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    table = "customers"
    fields = "customername, contactname, address, city, postalcode, country"
    values = "('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore')"
    sqlquery = "insert into " + table + " (" + fields + " ) values " + values
    with con.cursor() as cur:
        cur.execute(sqlquery)


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("select * from customers")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("select * from customers where country = 'Germany';")
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    with con.cursor() as cur:
        cur.execute("update customers set customername = 'Johnny Depp' "
                    "where customerid = (select min(customerid) from customers);")


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    with con.cursor() as cur:
        cur.execute("delete from customers  where customerid = (select max(customerid) from customers);")


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("select country from suppliers;")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute("select country from suppliers order by country desc;")
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    cur.execute("select count(city), city  from customers group by city order by count(city) desc;")
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("select count(country), country from customers group by country having count(country) > 10;")
    return cur.fetchall()
    pass


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("select * from customers order by customerid asc limit 10;")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("select * from customers where customerid >11;")
    return cur.fetchall()



def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    #cur.execute("select * from suppliers where country in ('USA', 'UK', 'Japan');")
    cur.execute("select * from suppliers where country = 'USA' and country = 'UK' and country = 'Japan';")

    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    #cur.execute("select * from products inner join suppliers ;")
    cur.execute("select products.productName from suppliers "
                "inner join products on suppliers.supplierId = products.supplierid where country = 'Sweden';")

    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute("select products.productId, products.productName, products.unit, products.price, suppliers.country," 
        " suppliers.city, suppliers.suppliername"
        " from products inner join suppliers on products.supplierid = suppliers.supplierId;")
    return cur.fetchall()



def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute("select customers.customername, customers.contactname, customers.country, orders.orderid "
                "from Customers inner join orders on customers.customerid = orders.customerid;")
    return cur.fetchall()



def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    # cur.execute("SELECT Customers.customername, Customers.address, Customers.Country, Suppliers.country, Suppliers.suppliername "
    #             "FROM Customers FULL JOIN Suppliers ON Customers.country = Suppliers.country "
    #             "order by customers.country;")
    cur.execute(
        "SELECT Customers.customername, Customers.address, Customers.Country as customercountry, "
        "Suppliers.country as suppliercountry, Suppliers.suppliername  "
        "FROM Customers FULL JOIN Suppliers ON Customers.country = Suppliers.country "
        "order by customers.country, Suppliers.country;")
    return cur.fetchall()

