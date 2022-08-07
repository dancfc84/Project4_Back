
from flask import Blueprint, request, g
from http import HTTPStatus


from models.authors import AuthorModel

from serializers.authors import AuthorSchema

from marshmallow.exceptions import ValidationError

from middleware.secure_route import secure_route


author_schema = AuthorSchema()

#Creates possible route
router = Blueprint("authors", __name__)

@router.route("/authors", methods=["GET"])
def get_authors():
    authors = AuthorModel.query.all()
    return author_schema.jsonify(authors, many=True), HTTPStatus.OK


@router.route("/authors/create", methods=["POST"])
@secure_route
def create_author():

    author_dictionary = request.json
    print(author_dictionary)

    try:
        author = author_schema.load(author_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "something went wrong" }

    author.save()

    return author_schema.jsonify(author), HTTPStatus.CREATED

    
@router.route("/authors/<int:author_id>", methods=["GET"])
def get_single_author(author_id):

    author = AuthorModel.query.get(author_id)

    if not author:
      return { "message": "author not found"}, HTTPStatus.OK

    return author_schema.jsonify(author)


@router.route("/authors/<int:author_id>", methods=["DELETE"])
@secure_route
def delete_single_author(author_id):

    existing_author = AuthorModel.query.get(author_id)

    if not existing_author:
      return {"message": "author not found"}, HTTPStatus.NOT_FOUND
    
    try:
        existing_author.remove()

    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}

    return author_schema.jsonify(existing_author), HTTPStatus.OK



@router.route("/authors/<int:author_id>", methods=["PUT"])
@secure_route
def update_single_author(author_id):
  
    author_dictionary = request.json
    existing_author = AuthorModel.query.get(author_id)
    print(author_dictionary)

    if not existing_author:
      return {"message": "comment not found"}, HTTPStatus.NOT_FOUND

    try:
        author = author_schema.load(
            author_dictionary, #new information, fields you are changing
            instance=existing_author, #existing record
            partial=True # lets SQL know to only update fields that I am providing
      )

    except ValidationError as e:
        return { "errors": e.messages, "messages": "something went wrong"}
    
    author.save()

    return author_schema.jsonify(author), HTTPStatus.OK


    