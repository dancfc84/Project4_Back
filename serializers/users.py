from app import ma
from models.users import UserModel
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = UserModel
        #If you don't have load_instance it will return a dictionary instead of a model in controllers
        load_instance = True
        #Can exclude columns when returning json, make sure hash can't be returned
        exclude = ("password_hash", "password")
        #Only include these columns in .load method..
        load_only = ("password")

# ! Tells serializer to expect a password field
# ! (in other words, because it's a column in User but don't have the column in our UserModel because its hidden)

    password = fields.String(required=True)