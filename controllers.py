from endpoints import Controller
from endpoints.decorators import route
import sqlite3
import json

def db_connection():
    conn = sqlite3.connect('87labs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, height REAL, length REAL , width REAL, weight REAL, price REALT) ''')
    conn.commit()
    return conn


class Default(Controller):
    @route(lambda req: len(req.path_args) == 0)
    def GET_1(self):
        conn = db_connection()
        c = conn.cursor()
        product_query = c.execute('''SELECT * FROM products''').fetchall()
        products = []
        for product in product_query:
            dict_product ={
                "id": product[0],
                "name" : product[1],
                "height": product[2],
                "length": product[3],
                "width": product[4],
                "weight": product[5],
                "price": product[6]
            }
            products.append(dict_product)
        conn.close()
        return products


    @route(lambda req: len(req.path_args) == 1)
    def GET_2(self, id):
        conn = db_connection()
        c = conn.cursor()
        result = c.execute('''SELECT * FROM products WHERE id = ?''', [id,]).fetchone()
        product = {
            'id' : result[0],
            'name' : result[1],
            'height': result[2],
            'length': result[3],
            'width': result[4],
            'weight': result[5],
            'price': result[6]
        }
        return product

    def POST(self, **kwargs):
        conn = db_connection()
        name = kwargs['name']
        height = kwargs['height']
        length = kwargs['length']
        width = kwargs['width']
        weight = kwargs['weight']
        price = kwargs['price']
        c = conn.cursor()
        c.execute('''INSERT INTO products(name, height, length, width, weight, price) VALUES(?,?,?,?,?,?)''', [name, height, length, width, weight, price])
        conn.commit()
        p =c.lastrowid
        product = {
            'id': p
        }
        conn.close()
        return product


class Tax(Controller):
    def POST(self, **kwargs):
        name = kwargs['name']
        height = float(  kwargs['height'])
        length = float( kwargs['length'])
        width = float(kwargs['width'])
        weight = float(kwargs['weight'])
        price = float(kwargs['price'])
        volume = height * length * width
        peso = volume * 300

        if peso <= 100:
            tax = price * 0.05

        else:
            tax = peso * (weight/1000)

        return { "tax" : tax,}