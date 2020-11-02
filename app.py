from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister
app = Flask(__name__)
app.secret_key = 'Aman'
api = Api(app)
jwt = JWT(app, authenticate, identity)
items = []
class Item(Resource):
    # @jwt_required()
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = 'This filed cant be left blank'
    )
    def get(self, name):
        # for i in items:
        #     if i['name'] == name:
        #         return i
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item": item}, 200 if item else 404
    # @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message':'Item {} Already Exist'.format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name':name, 'price': data['price']}
        items.append(item)
        return item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {"message" : "item deleted"}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type = float,
            required = True,
            help = 'This filed cant be left blank'
        )
        data = Item.parser.parse_args()
        item = next(filter(lambda x : x['name'] == name, items), None)
        if item is None:
            item = {'name' : name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item, 201
class ItemList(Resource):
    # @jwt_required()
    def get(self):
        return {'items':items}
    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
app.run(debug = True)