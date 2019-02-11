"""http://flask.pocoo.org/docs/1.0/config/#instance-folders"""


class Config:
    SECRET_KEY = ''
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost/tylerguo'  # May need to change to upload


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test:password@postgres:5432/testdb'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test:password@postgres:5432/testdb'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
