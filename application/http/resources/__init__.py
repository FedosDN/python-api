from flask_restful import Resource
from app import api


class Driver(Resource):
    def get(self):
        return 'Driver is here'


api.add_resource(Driver, '/test')
