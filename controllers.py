from endpoints import Controller
from endpoints.decorators import param
import sqlite3
import json

def db_connection():
    conn = sqlite3.connect('87labs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products (id INT PRIMARY KEY AUTOINCREMENT, name TEXT, height REAL, length REAL , width REAL, weight REAL, price REALT) ''')
    conn.commit()
    return conn

class Default(Controller):
    def GET(self):
        conn = db_connection()
        c = conn.cursor()
        products = c.execute('''SELECT * FROM products''').fetchall()

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
        c.execute('''INSERT INTO products()''')
        product = {
            'name': name,
            'height': height,
            'length': length,
            'width': width,
            'weigth' : weight,
            'price' : price
        }
        return product


class Tax(Controller):
    pass