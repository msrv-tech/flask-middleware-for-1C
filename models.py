from extensions import db
from sqlalchemy import event
from sqlalchemy.orm import relationship


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

    # Исправляем определение отношения
    images = relationship(
        'ProductImage',
        backref='product',
        cascade='all, delete-orphan',
        order_by='ProductImage.id'
    )


class ProductImage(db.Model):
    __tablename__ = 'product_images'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    is_main = db.Column(db.Boolean, default=False)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('products.id', ondelete='CASCADE'),
        nullable=False
    )


# Перемещаем обработчик события после определения классов
@event.listens_for(Product.images, 'append')
def check_main_image(target, value, initiator):
    if value.is_main:
        for img in target:
            if img != value:
                img.is_main = False