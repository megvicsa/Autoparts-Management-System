from datetime import datetime
from sql_connection import get_sql_connection

def insert_new_order(connection, order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO `CS348-Information-System`.orders" "(customer_name, total_price, date)" " VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['total_price'], datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO `CS348-Information-System`.order_details" "(order_id, product_id, quatity, price)" "VALUES (%s, %s, %s, %s)")

    order_details_data = []

    for order_detail_log in order['order_details']:
        order_details_data.append([
            order_id, int(order_detail_log['product_id']), float(order_detail_log['quatity']), float(order_detail_log['total_price'])
        ])
    
    cursor.executemany(order_details_query, order_details_data)
    connection.commit()
    return order_id


def get_order_details(connection, order_id):
    cursor = connection.cursor()
    query = """
    SELECT od.order_id, od.quatity, p.name AS product_name, p.price
    FROM `CS348-Information-System`.order_details AS od
    JOIN `CS348-Information-System`.products AS p ON od.product_id = p.product_id
    WHERE od.order_id = %s
    """
    cursor.execute(query, (order_id,))
    records = []
    for (order_id, quatity, product_name, price) in cursor:
        records.append({
            'order_id': order_id,
            'quatity': quatity,
            'product_name': product_name,
            'price': price
        })
    cursor.close()
    return records


def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM `CS348-Information-System`.orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total_price, date) in cursor :
        response.append({
            'order_id' : order_id,
            'customer_name' : customer_name,
            'total_price' : total_price,
            'date' : date
        })
    return response

def get_total_sales_per_day(connection):
    cursor = connection.cursor()
    query = """
    SELECT DATE(date) as date, SUM(total_price) as total_sales FROM `CS348-Information-System`.orders GROUP BY DATE(date);
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_top_selling_products(connection):
    cursor = connection.cursor()
    query = """
    SELECT p.name, SUM(od.quatity) as total_quatity
    FROM `CS348-Information-System`.order_details od
    JOIN `CS348-Information-System`.products p ON od.product_id = p.product_id
    GROUP BY p.product_id, p.name
    ORDER BY total_quatity DESC
    LIMIT 10;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    converted_result = [(name, int(quatity)) for name, quatity in result]
    return converted_result

def get_average_order_value(connection):
    cursor = connection.cursor()
    query = """
    SELECT AVG(total_price) as avg_order_value
    FROM `CS348-Information-System`.orders;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_top_selling_products(connection))
    # Example usage of getting order details for order_id 4
    # print(get_order_details(connection, 1268))
    # Example usage of inserting a new order
    # print(insert_new_order(connection, {
    #     'customer_name': 'shubham',
    #     'total_cost' : '600',
    #     'order_details' : [
    #         {'product_id' : 1,
    #         'quatity' : 1,
    #         'price' : 281
    #         }
            
    #     ]
    # }))
   
