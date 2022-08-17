
from flask import Blueprint, request, g, jsonify
from http import HTTPStatus

from app import db
from models.genres import GenreModel

from serializers.genres import GenreSchema

from marshmallow.exceptions import ValidationError


genre_schema = GenreSchema()

#Creates possible route
router = Blueprint("genres", __name__)

@router.route("/genres", methods=["GET"])
def get_genres():

    text = f"SELECT * FROM genres ORDER BY genre"
    try:
        records = db.engine.execute(text)

        if not records:
            return { "message": "No records found"}, HTTPStatus.OK

        results_list = [] 
        for r in records:
            r_dict = dict(r.items())
            print(r_dict)
            results_list.append(r_dict)

        return jsonify(results_list), HTTPStatus.OK

    except Exception as e:

        return {"messages" : "Something went wrong"}


