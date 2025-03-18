from flask import Flask
from config import Config
from extensions import db, migrate
from models import User, Product  # Импорт моделей после инициализации


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)

    # Импорт API маршрутов
    from api.products import products_bp
    app.register_blueprint(products_bp)

    from api.cart import cart_bp
    app.register_blueprint(cart_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001)