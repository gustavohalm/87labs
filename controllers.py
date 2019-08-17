from endpoints import Controller
from endpoints.decorators import param
import sqlite3
import json

def db_connection():
    conn = sqlite3.connect('87labs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, height REAL, length REAL , width REAL, weight REAL, price REALT) ''')
    conn.commit()
    return conn

class Default(Controller):
    def GET(self):
        conn = db_connection()
        c = conn.cursor()
        product_query = c.execute('''SELECT * FROM products''').fetchall()
        products = []
        for product in product_query:
            dict_product ={
                "name" : product[0],
                "height": product[1],
                "length": product[2],
                "width": product[3],
                "weight": product[4],
                "price": product[5]
            }
            products.append(dict_product)
        conn.close()
        return products

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
        product = {
            'name': name,
            'height': height,
            'length': length,
            'width': width,
            'weigth' : weight,
            'price' : price
        }
        conn.close()
        return product


class Tax(Controller):
    pass