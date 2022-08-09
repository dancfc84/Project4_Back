from flask import Blueprint, request, jsonify
from models.users import UserModel
from serializers.users import UserSchema
from marshmallow.exceptions import ValidationError
from sqlalchemy.orm.session import make_transient_to_detached

from middleware.secure_route import secure_route

from http import HTTPStatus

user_schema = UserSchema()

router = Blueprint("users", __name__)

@router.route("/register", methods=["POST"])
def register():

    try:    
        user_dictionary = request.json
        print(user_dictionary)
        user = user_schema.load(user_dictionary)
        user.credits = 2
        user.rating = 4
        user.save()


    except AssertionError as e:
        return jsonify(msg="Error: {}. ".format(e))
    
    except Exception as e:
        return { "messages": "Something went wrong" }, HTTPStatus.BAD_REQUEST
    
    try:
        user_login = UserModel.query.filter_by(email=user_dictionary["email"]).first()

        if not user_login:
            return {"message": "No user found for this email"}

        if not user_login.validate_password(user_dictionary["password"]):
            return {"message": "You are not authorised"}, HTTPStatus.UNAUTHORIZED

        token = user.generate_token()
        return {"token": token, "message": "Welcome Back"}

    except Exception as e:

        return {"messages" : "Something went wrong"}


@router.route("/login", methods=["POST"])
def login():
    try:
        credentials_dictionary = request.json
        user = UserModel.query.filter_by(email=credentials_dictionary["email"]).first()

        if not user:
            return {"message": "No user found for this email"}

        if not user.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not authorised"}, HTTPStatus.UNAUTHORIZED

        token = user.generate_token()
        return {"token": token, "message": "Welcome Back"}

    except Exception as e:

        return {"messages" : "Something went wrong"}


@router.route("/users", methods=["GET"])
@secure_route
def get_users():
    users = UserModel.query.all()

    if not users:
        return {"message": "Users not found"}, HTTPStatus.NOT_FOUND

    return user_schema.jsonify(users, many=True), HTTPStatus.OK



@router.route("/users/<int:user_id>", methods=["GET"])
@secure_route
def get_user(user_id):
    user = UserModel.query.get(user_id)
    print(user)

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    
    return user_schema.jsonify(user), HTTPStatus.OK


@router.route("/users/<int:user_id>", methods=["PUT"])
@secure_route
def update_user(user_id):

    user_dictionary = request.json
    existing_user = UserModel.query.get(user_id)

    if not existing_user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    
    try:
        user = user_schema.load(
            user_dictionary, #new information, fields you are changing
            instance=existing_user, #existing record
            partial=True # lets SQL know to only update fields that I am providing
      )

    except ValidationError as e:
        return { "errors": e.messages, "messages": "something went wrong"}
    
    user.save()

    return user_schema.jsonify(user), HTTPStatus.OK
