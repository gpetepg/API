from flask import Blueprint
from flask_restplus import Api

blueprint = Blueprint('website', __name__, template_folder='templates')
api = Api(blueprint)


@blueprint.route('/')
def homepage():
    return('hello')


@blueprint.route('/dogs/')
def dog():
    return('dogs')


