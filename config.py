import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SESSION_TYPE = 'filesystem'  # или 'redis' для продакшена
    SESSION_PERMANENT = False