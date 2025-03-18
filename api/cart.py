from flask import Blueprint, request, session
from extensions import db
from models import Product

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    cart = session.get('cart', {})

    if not Product.query.get(product_id):
        return {'error': 'Product not found'}, 404

    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return {'success': True}


@cart_bp.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        session['cart'] = cart
    return {'success': True}