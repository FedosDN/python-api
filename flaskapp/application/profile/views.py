from app import app
from .models import DriverProfile
from .schema.driver import DriverProfileSchema


driver_schema = DriverProfileSchema()


@app.route('/drivers')
def drivers():
    driver = DriverProfile.query.get(1)
    return driver_schema.dump(driver)

from flask_restful import Resource
from flask_restful import fields, marshal_with, reqparse

driver_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
}
post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'username', dest='username',
    location='form', required=True,
    help='The user\'s username',
)

from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email(required=True)

user_schema = UserSchema()
from flask import request

class CreateUpdateDriver(Resource):

    def get(self,id):
        pass
    def post(self):
        #args = post_parser.parse_args()
        #print(request.form)
        errors = user_schema.validate(request.form)
        if errors:  
            print(errors)
        return {'status': 0}
