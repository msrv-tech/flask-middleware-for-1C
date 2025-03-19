from flask import Flask, render_template, session
from config import Config
from extensions import db, migrate
from api.products import products_bp
from api.cart import cart_bp
from api.images import images_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация API
    app.register_blueprint(products_bp, url_prefix='/api')
    app.register_blueprint(cart_bp, url_prefix='/api')
    app.register_blueprint(images_bp, url_prefix='/api/v1')

    # Веб-маршруты
    @app.route('/')
    def index():
        from models import Product
        products = Product.query.all()
        return render_template('index.html', products=products)

    @app.route('/cart')
    def cart():
        from models import Product
        cart_items = session.get('cart', {})

        # Получаем полную информацию о товарах
        products = {}
        for product_id in cart_items.keys():
            product = Product.query.get(int(product_id))
            if product:
                products[product_id] = {
                    'name': product.name,
                    'price': product.price,
                    'quantity': cart_items[product_id]
                }

        return render_template('cart.html', products=products)

    @app.route('/product/<int:product_id>')
    def product_detail(product_id):
        from models import Product
        product = Product.query.get_or_404(product_id)
        return render_template('product_detail.html', product=product)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Создаст все таблицы, если их нет
    app.run(host='0.0.0.0', port=5000, debug=True)