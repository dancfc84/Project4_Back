
from flask import Blueprint, request, g
from http import HTTPStatus


from models.genres import GenreModel

from serializers.genres import GenreSchema

from marshmallow.exceptions import ValidationError


genre_schema = GenreSchema()

#Creates possible route
router = Blueprint("gentres", __name__)

@router.route("/genres", methods=["GET"])
def get_genres():
    
    try:
        genres = GenreModel.query.all()
        
    except ValidationError as e:
        return { "errors": e.messages, "message": "something went wrong" }

    return genre_schema.jsonify(genres, many=True), HTTPStatus.OK

