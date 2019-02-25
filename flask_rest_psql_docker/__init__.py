"""http://flask.pocoo.org/docs/1.0/tutorial/factory/"""

from flask import Flask
from flask_rest_psql_docker.extensions import db, ma, migrate
import flask_rest_psql_docker.config as configure
import os


def create_app(config=None):
    # create app
    app = Flask(__name__)

    # Set config
    if config == 'testing':
        app.config.from_object(configure.TestingConfig)
    elif config == 'development':
        app.config.from_object(configure.DevelopmentConfig)
    elif config == 'production':
        app.config.from_object(configure.ProductionConfig)
    else:
        raise ValueError('Incorrect configuration')

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
