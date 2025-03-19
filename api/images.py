from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from extensions import db
from models import ProductImage
from utils import allowed_file, save_uploaded_files
from config import Config
import os

images_bp = Blueprint('images', __name__)


@images_bp.route('/products/<int:product_id>/images', methods=['POST'])
def upload_product_images(product_id):
    # Аутентификация (пример с JWT)
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Missing or invalid token'}), 401

    token = auth_header.split(" ")[1]
    # Здесь должна быть проверка JWT токена
    # if not validate_token(token):
    #     return jsonify({'error': 'Invalid token'}), 401

    if 'images' not in request.files:
        return jsonify({'error': 'No files part'}), 400

    files = request.files.getlist('images')
    if len(files) == 0:
        return jsonify({'error': 'No selected files'}), 400

    try:
        saved_files = save_uploaded_files(files, product_id)

        # Сохраняем информацию в БД
        for filename in saved_files:
            image = ProductImage(
                filename=filename,
                product_id=product_id,
                is_main=False
            )
            db.session.add(image)

        db.session.commit()

        return jsonify({
            'status': 'success',
            'product_id': product_id,
            'uploaded_files': saved_files
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500