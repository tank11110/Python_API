from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:123@db:5432/test_db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    size = db.Column(db.String(80), nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(80), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'category': self.category,
            'size': self.size,
            'unit_price': self.unit_price,
            'inventory': self.inventory,
            'color': self.color,
        }

def initialize_db():
    retries = 5
    while retries:
        try:
            db.create_all()
            break
        except OperationalError:
            retries -= 1
            print(f"Trying connect db ({5 - retries}/5)")
            time.sleep(5)
    else:
        print("Connect failed")

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello API Project'})

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products])

@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.serialize())

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return jsonify(product.serialize())

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'})

if __name__ == '__main__':
    with app.app_context():
        initialize_db()
    app.run(debug=True, host='0.0.0.0')
