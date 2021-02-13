from flask import request, jsonify
from functools import wraps
import jwt
import os
from app import app
from ..profile.models import User

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({
                'status': 403,
                'message': 'a valid token is missing'
                })

        #print(token)
        

        # keypath = os.path.join(app.instance_path, 'pub-key.txt')
        
        with open('pub-key.txt') as file:
            key = file.read()
        #print(key)
        #print(token)
        data = jwt.decode(token, key , algorithms=["RS256"])
        print(data)
        current_user = User.query.filter_by(id=int(data['sub'])).first()
        print(current_user)
        
        return f(*args, **kwargs)

        # try:
        #     data = jwt.decode(token, app.config[SECRET_KEY])
        #     current_user = Users.query.filter_by(public_id=data['public_id']).first()
        # except:
        #     return jsonify({'message': 'token is invalid'})
        #
        # return f(current_user, *args, **kwargs)

    return decorator