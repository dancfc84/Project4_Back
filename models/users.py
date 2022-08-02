from datetime import datetime
from app import db, bcrypt
from models.base import BaseModel
from datetime import datetime, timedelta
from config.environment import secret

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates 

# ! Import jwt library (this is pyjwt)
import jwt
import re

class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    address1 = db.Column(db.Text, nullable=False)
    address2 = db.Column(db.Text)
    county = db.Column(db.Text)
    postcode = db.Column(db.Text, nullable=False)
    credits = db.Column(db.Integer)
    rating = db.Column(db.Float)

    password_hash = db.Column(db.Text, nullable=True)

    # We want to set a password field that doesn't get saved to the db
    # Hybrid this will ensure you can provide a password field that won't get saved

    @hybrid_property
    def password(self):
        pass

    #the password.setter decorator runs before we save the password, takes the password given as an argument
    @password.setter
    def password(self, password_plaintext):

    #validation password

        if not password_plaintext:
            raise AssertionError('Password not provided')
        if not re.match('\d.*[A-Z]|[A-Z].*\d', password_plaintext):
            raise AssertionError('Password must contain 1 capital letter and 1 number')
        if len(password_plaintext) < 8 or len(password_plaintext) > 50:
            raise AssertionError('Password must be between 8 and 50 characters')

        #This will hash the password
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)

        #Store hashed password in database
        self.password_hash = encoded_pw.decode("utf-8")

    def validate_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password_hash, plaintext_password)


    def generate_token(self):

        #Payload is the data in the body of the token
        payload = {
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow(),
            "sub": self.id
        }

        token = jwt.encode(
            payload, 
            secret, 
            algorithm="HS256"
        )

        return token


    #Validation decorators
    @validates("username")
    def validate_username(self, key, username):
        if not username:
            raise AssertionError("no username provided")
        if len(username) < 5 or len(username) > 20:
            raise AssertionError("Username must be between 5 and 20 characters")

        return username


    @validates("email")
    def validate_email(self, key, email):
        if not email:
            raise AssertionError("No email provided")

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')

        return email
