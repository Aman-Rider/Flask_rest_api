from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Item(Resource):
    # @jwt_required()
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = 'This filed cant be left blank'
    )
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE NAME=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            return  {'item':{'name': row[0], 'price':  row[1]}}
        else:
            return {'message' : 'Item not found'}, 404
    # @jwt_required()
    def post(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE NAME=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row is not None:
            return {'message':'Item {} Already Exist'.format(name)}, 400
        data = Item.parser.parse_args()
        # item = {'name':name, 'price': data['price']}
        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (name, data['price']))
        connection.commit()
        connection.close()
        return {"message": "New Item created"}, 201
    
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE NAME=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {"message" : "item deleted"}

    def put(self, name):
        data = Item.parser.parse_args()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE NAME=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row is None:
            query = "INSERT INTO items VALUES(?,?)"
            cursor.execute(query, (name, data['price']))
        else:
            query = "UPDATE items SET price=? where name=?"
            cursor.execute(query, (data['price'], name))
        connection.commit()
        connection.close()
        return {"message":"Item Updated"}, 201
class ItemList(Resource):
    # @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()
        # items = []
        return {'items':row}
    