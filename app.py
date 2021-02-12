from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv, dotenv_values


def create_app():
    c_app = Flask(__name__)
    load_dotenv()
    c_app.config.update(dotenv_values())
    return c_app


def create_db(c_app):
    return SQLAlchemy(c_app)


def create_marshmallow(c_app):
    return Marshmallow(c_app)


def create_api(c_app):
    return Api(c_app)


def create_jwt(c_app):
    c_app.config['JWT_SECRET_KEY'] = 'Dude!WhyShouldYouEncryptIt'
    c_app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    return JWTManager(c_app)


app = create_app()
db = create_db(app)
ma = create_marshmallow(app)
jwt = create_jwt(app)

api = create_api(app)


@jwt.token_in_blacklist_loader
def check_jwt(decrypted_token):
    jti = decrypted_token['jti']
    print(jti)
    pass
