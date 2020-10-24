from flask import Flask, jsonify, request, render_template
from datetime import datetime
app = Flask(__name__)

stores = [
    {
        'name' : "my Store",
        'items': [
            {
                'name' : 'my item',
                'price': 10
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)
@app.route('/store/<string:name>')
def get_store(name):
    for i in stores:
        if i['name'] == name:
            return jsonify(i)
    return jsonify({'message':'Store not found!!!'})
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    print(request_data)
    print('----')
    for i in stores:
        if i['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            i['items'].append(new_item)
            return jsonify(i)
    return jsonify({'message':'Store not found!!!'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for i in stores:
        if i['name'] == name:
            return jsonify({'items': i['items']})
    return jsonify({'message':'Store not found!!!'})

if __name__ == "__main__":
    app.run() 