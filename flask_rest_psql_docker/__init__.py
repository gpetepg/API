from flask import Flask
from flask_rest_psql_docker.api.models import db, ma


app = Flask(__name__)

db.init_app(app)
ma.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://testusr:password@localhost:5432/testdb'

# Register blueprints; import below db to avoid circular errors
from flask_rest_psql_docker.api.routes import blueprint as api
from flask_rest_psql_docker.website.routes import blueprint as website

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(website, url_prefix='')
