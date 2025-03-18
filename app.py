from flask import Flask, render_template, session
from config import Config
from extensions import db, migrate
from api.products import products_bp
from api.cart import cart_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация API
    app.register_blueprint(products_bp, url_prefix='/api')
    app.register_blueprint(cart_bp, url_prefix='/api')

    # Веб-маршруты
    @app.route('/')
    def index():
        from models import Product
        products = Product.query.all()
        return render_template('index.html', products=products)

    @app.route('/cart')
    def cart():
        cart_items = session.get('cart', {})
        return render_template('cart.html', cart=cart_items)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)