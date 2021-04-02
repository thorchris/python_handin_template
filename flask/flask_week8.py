from flask import Flask, jsonify, abort, request
app = Flask(__name__)

import mysql.connector as mysql
cnx = mysql.connect(host = "db", user = "root", passwd = "root", db = "db")

@app.route('/api/laptops/all', methods=['GET'])
def get_task():
    cursor = cnx.cursor()
    query = "SELECT * FROM laptops"
    cursor.execute(query)
    laptops = cursor.fetchall()
    res = []

    for idx, val in enumerate(laptops):
        res.append({"id": val[0], "name": val[1], "price": val[2]})

    return jsonify(res)

@app.route('/api/laptops', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    name = request.json['name']
    price = request.json['price']
    laptop = {
        'name': request.json['name'],
        'price': request.json['price'],
    }
    cursor = cnx.cursor()
    query = """INSERT INTO laptops (name, price) VALUES (%s, %s)"""
    val = (name, price,)
    cursor.execute(query, val) 
    cnx.commit()
    cursor.close()
    return jsonify(laptop), 201