# utils.py
import os
from werkzeug.utils import secure_filename
from config import Config


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def save_uploaded_files(files, product_id):
    saved_files = []
    upload_dir = os.path.join(Config.UPLOAD_FOLDER, str(product_id))

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(upload_dir, filename)
            file.save(file_path)
            saved_files.append(filename)

    return saved_files