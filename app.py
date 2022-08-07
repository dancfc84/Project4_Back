
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config.environment import db_URI

from flask_marshmallow import Marshmallow

from flask_bcrypt import Bcrypt

#creating an instance of the Flask class
app = Flask(__name__)

#Configuring it with flask
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

#removes a warning for an unused part of the library
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print(app)

#Instantiate flask plug-ins

db = SQLAlchemy(app)

#Creating an instance of Marshmallow
ma = Marshmallow(app)

bcrypt = Bcrypt(app)



#Import controllers here
from controllers import books
from controllers import users
from controllers import authors
from controllers import genres

#Put routes here
app.register_blueprint(books.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")
app.register_blueprint(authors.router, url_prefix="/api")
app.register_blueprint(genres.router, url_prefix="/api")