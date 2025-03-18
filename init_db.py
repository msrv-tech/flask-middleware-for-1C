from app import create_app
from extensions import db
from models import Product

app = create_app()

with app.app_context():
    db.create_all()

    # Добавление тестовых товаров
    if not Product.query.first():
        products = [
            Product(name="iPhone 15", price=999.99),
            Product(name="MacBook Pro", price=2499.99)
        ]
        db.session.add_all(products)
        db.session.commit()
        print("Added test products!")