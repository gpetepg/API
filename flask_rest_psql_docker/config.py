"""http://flask.pocoo.org/docs/1.0/config/#instance-folders"""
import os


class Config:
    SECRET_KEY = 'superSecret'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost/tylerguo'  # May need to change to upload
    UPLOAD_FOLDER = os.environ.get('SITE_UPLOADS')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test:password@postgres:5432/testdb'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test:password@postgres:5432/testdb'
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
