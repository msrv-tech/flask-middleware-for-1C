from flask import Blueprint, jsonify
from extensions import db
from models import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([{
            'id': p.id,
            'name': p.name,
            'price': p.price
        } for p in products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500