from sql_connection import get_sql_connection

def get_all_products(connection):
    
    cursor = connection.cursor()

    query = ("select products.product_id, products.name, products.brand_id, products.price, brand.name " 
            "from products inner join brand on products.brand_id=brand.brand_id")
    
    cursor.execute(query)

    reponse = []

    for (product_id, product_name, brand_id, price, brand_name) in cursor:
        reponse.append(
            {
                'product_id' : product_id,
                'name' : product_name,
                'brand_id' : brand_id,
                'price' : price,
                'brand_name' : brand_name
            }
        )
    return reponse

def insert_new_product(connection, product) :
    cursor = connection.cursor()
    query = ("INSERT INTO `CS348-Information-System`.`products` (name, brand_id, price)  values (%s, %s, %s)")
    data = (product['product_name'], product['brand_id'], product['price'])
    cursor.execute(query, data) 
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM `CS348-Information-System`.`products` WHERE product_id = %s")
    cursor.execute(query, (product_id,))
    connection.commit()
    return cursor.lastrowid

def update_product(connection, product_id, product_data):
    cursor = connection.cursor()
    query = ("UPDATE `CS348-Information-System`.`products` "
             "SET name = %s, brand_id = %s, price = %s "
             "WHERE product_id = %s")
    try:
        data = (product_data['product_name'], product_data['brand_id'], product_data['price'], product_id)
        cursor.execute(query, data)
        connection.commit()
        return cursor.rowcount
    except Exception as e:
        print(f"Error updating product: {str(e)}")
        return 0


if __name__=='__main__':
    connection = get_sql_connection()
    # print(update_product(connection, 10))
    # product_data = {
    #     'product_name': 'car door',
    #     'brand_id': 82,  
    #     'price': 300.00
    # }

    # Example product_id
    # product_id = 21  

    # Update the product
    # updated_product_id = update_product(connection, product_id, product_data)
    # print("Updated Product ID:", updated_product_id)