from http import HTTPStatus
import jwt

from functools import wraps
from flask import request, g

from models.users import UserModel
from config.environment import secret

def secure_route(route_func):
    @wraps(route_func)
    def decorated_function(*args, **kwargs):
        #Getting token from header sent
        raw_token = request.headers.get("Authorization")

        if not raw_token:
            return {"message": "Unauthorized1"}, HTTPStatus.UNAUTHORIZED
        # ! Clean up token
        clean_token = raw_token.replace("Bearer ", "")

        try:
            payload = jwt.decode(clean_token, secret, "HS256")

            user_id = payload["sub"]

            user = UserModel.query.get(user_id)

            if not user:
                return {"message": "Unauthorized2"}, HTTPStatus.UNAUTHORIZED

            # ! Setting current_user as a global variable, so I can access it in my controllers
            g.current_user = user

        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED

        except Exception as e:
            return {"message": "Unauthorized3"}, HTTPStatus.UNAUTHORIZED

        return route_func(*args, **kwargs)


    return decorated_function        
