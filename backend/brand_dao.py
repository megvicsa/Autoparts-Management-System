
def get_brand(connection):
    cursor = connection.cursor()
    query = ("select * from `CS348-Information-System`.brand")
    cursor.execute(query)
    response = []
    for (brand_id, name) in cursor:
        response.append({
            'brand_id': brand_id,
            'name': name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_brand(connection))