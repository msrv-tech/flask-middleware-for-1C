from app import create_app
from models import Product, ProductImage
from extensions import db

app = create_app()

with app.app_context():
    # Создаем тестовый товар
    p = Product(
        name="iPhone 15",
        price=999.99,
        description="Новый смартфон от Apple"
    )
    db.session.add(p)
    db.session.commit()

    # Добавляем изображения
    images = [
        ProductImage(filename="iphone1.jpg", product_id=p.id, is_main=True),
        ProductImage(filename="iphone2.jpg", product_id=p.id)
    ]
    db.session.add_all(images)
    db.session.commit()