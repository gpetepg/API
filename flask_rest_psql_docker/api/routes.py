from flask import Blueprint
from flask_restplus import Api, Resource
from flask import jsonify

from .models import People, PeopleSchema


blueprint = Blueprint('api', __name__, template_folder='templates')
api = Api(blueprint)

ns_ppl = api.namespace('people', description='People Information')
ns_dogs = api.namespace('dogs', description='Dog Information')


@ns_ppl.route("/")
class PeopleList(Resource):
    
    def get(self):
        """returns a list of people"""
        
        person = People.query.first()
        schema = PeopleSchema()
        output = schema.dump(person).data

        return jsonify({'user': output})

    def post(self):
        """Adds a new person to the list"""


@ns_ppl.route("/<int:id>")
class EndPeople(Resource):
    def get(self, id):
        """Displays a person's details"""

        person = People.query.filter_by(id=f'{id}').first()
        schema = PeopleSchema()
        output = schema.dump(person).data

        return jsonify({'user': output})

    def put(self, id):
        """Edits a selected person"""


@ns_dogs.route("/")
class DogsList(Resource):
    
    def get(self):
        """returns a list of dogs"""

    def post(self):
        """Adds a new dog to the list"""


@ns_dogs.route("/<int:id>")
class Dogs(Resource):
    
    def get(self, id):
        """Displays a dog's details"""
        
    def put(self, id):
        """Edits a selected dog"""

