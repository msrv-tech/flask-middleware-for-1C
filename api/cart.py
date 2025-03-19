from flask import Blueprint, request, session, jsonify
from models import Product

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/cart', methods=['POST'])
def add_to_cart():
    try:
        product_id = request.json.get('product_id')
        if not product_id:
            return jsonify({'error': 'Missing product_id'}), 400

        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404

        cart = session.get('cart', {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        session['cart'] = cart

        return jsonify({
            'success': True,
            'cart_total': len(cart)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@cart_bp.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    try:
        cart = session.get('cart', {})
        product_key = str(product_id)

        if product_key in cart:
            del cart[product_key]
            session['cart'] = cart
            session.modified = True  # Важно для сохранения изменений
            return jsonify({'success': True})

        return jsonify({'error': 'Product not in cart'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500