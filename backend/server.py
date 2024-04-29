from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sql_connection
from flask_cors import CORS

# import mysql.connector
import json

import orders_dao
import brand_dao

app = Flask(__name__)
CORS(app)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getBrand', methods=['GET'])
def get_brand():
    brand = brand_dao.get_brand(connection)
    response = jsonify(brand)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    requestNew = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, requestNew)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    returnDelete = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': returnDelete
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_new_order():
    request_load = json.loads(request.form['data'])
    order_id = orders_dao.insert_new_order(connection, request_load)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/updateProduct/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    try:
        updated = products_dao.update_product(connection, product_id, data)
        if updated > 0:
            app.logger.info(f'Product {product_id} updated successfully.')
            return jsonify({'status': 'success', 'product_id': product_id, 'message': 'Product updated successfully'}), 200
        else:
            app.logger.warning(f'No product found with ID {product_id}.')
            return jsonify({'status': 'error', 'message': 'No product found with the given ID'}), 404
    except Exception as e:
        app.logger.error(f'Error updating product {product_id}: {str(e)}', exc_info=True)
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/salesReport', methods=['GET'])
def sales_report():
    total_sales = orders_dao.get_total_sales_per_day(connection)
    top_products = orders_dao.get_top_selling_products(connection)
    avg_order_value = orders_dao.get_average_order_value(connection)
    return jsonify({
        'total_sales_per_day': total_sales,
        'top_selling_products': top_products,
        'average_order_value': avg_order_value
    })


if __name__ == "__main__":
    print("APMS")
    app.run(port=3131)