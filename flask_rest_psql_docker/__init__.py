"""http://flask.pocoo.org/docs/1.0/tutorial/factory/"""
from flask import Flask
from flask_rest_psql_docker.extensions import db, ma, migrate
import os


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/tylerguo'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://test:password@postgres:5432/testdb'

    # Extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from .api.routes import blueprint as api
    from .website.routes import blueprint as website

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(website, url_prefix='')

    return app
