from flask import Blueprint
from extensions import db
from models import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def get_products():
    products = Product.query.all()
    # ... обработка и возврат данных