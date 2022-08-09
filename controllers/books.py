import json
import mimetypes
from flask import Blueprint, jsonify, request, g, Response
from http import HTTPStatus
from app import db

from models.books import BookModel
from models.book_listing import BookListingModel
from models.comments import CommentModel
from models.book_sale import book_sale

from serializers.books import BookSchema
from serializers.book_listing import BookListingSchema
from serializers.comments import CommentSchema

from marshmallow.exceptions import ValidationError

from middleware.secure_route import secure_route


book_schema = BookSchema()
book_listing_schema = BookListingSchema()
comment_schema = CommentSchema()


#Creates possible route
router = Blueprint("books", __name__)

@router.route("/books", methods=["GET"])

def get_books():

    text = f"SELECT * FROM books ORDER BY name"
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


@router.route("/books", methods=["POST"])
@secure_route
def create_book():

    book_dictionary = request.json

    try:
        book = book_schema.load(book_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "something went wrong" }

    book.user_id = g.current_user.id
    book.rating = 3
    book.genre_id = 1
    book.author_id = 1
    book.save()

    return book_schema.jsonify(book), HTTPStatus.CREATED

    
@router.route("/books/<int:book_id>", methods=["GET"])
def get_single_book(book_id):

    text = f"SELECT * FROM books JOIN authors ON books.author_id = authors.id WHERE books.id = {book_id}"
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


@router.route("/books/<int:book_id>", methods=["DELETE"])
@secure_route
def delete_single_book(book_id):

    existing_book = BookModel.query.get(book_id)

    if not existing_book:
      return {"message": "Book not found"}, HTTPStatus.NOT_FOUND

    if not g.current_user.id == existing_book.user_id:
      return {"message": "Not your book, hands off!"}, HTTPStatus.UNAUTHORIZED
    
    try:
        existing_book.remove()

    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}

    return book_schema.jsonify(existing_book), HTTPStatus.OK



@router.route("/books/<int:book_id>", methods=["PUT"])
@secure_route
def update_single_book(book_id):
  
    book_dictionary = request.json
    existing_book = BookModel.query.get(book_id)
    print(book_dictionary)

    if not existing_book:
      return {"message": "comment not found"}, HTTPStatus.NOT_FOUND

    if not g.current_user.id == existing_book.user_id:
        return {"message": "Not your book, hands off!"}, HTTPStatus.UNAUTHORIZED

    try:
        book = book_schema.load(
            book_dictionary, #new information, fields you are changing
            instance=existing_book, #existing record
            partial=True # lets SQL know to only update fields that I am providing
      )

    except ValidationError as e:
        return { "errors": e.messages, "messages": "something went wrong"}
    
    book.save()

    return book_schema.jsonify(book), HTTPStatus.OK


#Book Listing

@router.route("/books/<int:book_id>/listing", methods=["POST"])
@secure_route
def book_create_listing(book_id):

    listing_dictionary = request.json
    
    print(listing_dictionary)

    try:
        book_listing = book_listing_schema.load(listing_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "something went wrong" }

    book_listing.user_id = g.current_user.id
    book_listing.save()

    book = BookModel.query.get(book_id)
    book_listing = BookListingModel.query.get(book_listing.id)

    if not book or not book_listing:
        return {'message': "Item not found"}

    try:
        book.listing.append(book_listing)
        book.save()

    except ValidationError as e:
            return { "errors": e.messages, "message": "Something went wrong" }
            

    return book_listing_schema.jsonify(book_listing), HTTPStatus.CREATED



@router.route("/books/<int:book_id>/listing", methods=["GET"])
def book_listings(book_id):
    text = f"SELECT books.name, book_conditions.condition, book_types.type, users.username, book_listings.id, book_listings.user_id FROM book_sale JOIN book_listings ON book_sale.book_listings_id = book_listings.id JOIN books ON book_sale.book_id = books.id JOIN book_conditions ON book_listings.condition_id = book_conditions.id JOIN book_types ON book_listings.type_id = book_types.id JOIN users ON book_listings.user_id = users.id WHERE book_id = {book_id}"
    try:
        records = db.engine.execute(text)
            
        if not records:
            return { "message": "No records found"}, HTTPStatus.OK
    
        results_list = [] 
        for r in records:
            r_dict = dict(r.items())
            results_list.append(r_dict)
        return jsonify(results_list), HTTPStatus.OK

    except Exception as e:

        return {"messages" : "Something went wrong"}


@router.route("/listings/<int:listing_id>", methods=["DELETE"])
@secure_route
def del_book_listings(listing_id):
        book_listing = BookListingModel.query.get(listing_id)

        if not book_listing:
            return {"message": "Book not found"}, HTTPStatus.NOT_FOUND

        try:
            book_listing.remove()

        except ValidationError as e:
            return {"errors:": e.messages, "messages": "Something went wrong"}

        return book_schema.jsonify(book_listing), HTTPStatus.OK



#comments


@router.route("/books/<int:book_id>/comments/", methods=["GET"])
@secure_route
def book_comments( book_id ):

    text = f"SELECT comments.book_id, comments.content, comments.created_at, comments.id, users.username, comments.user_id FROM comments JOIN users ON comments.user_id = users.id WHERE book_id = {book_id}"
    try:
        records = db.engine.execute(text)

        if not records:
            return { "message": "No records found"}, HTTPStatus.OK

        results_list = [] 
        for r in records:
            r_dict = dict(r.items())
            results_list.append(r_dict)
        return jsonify(results_list), HTTPStatus.OK

    except Exception as e:

        return {"messages" : "Something went wrong"}


@router.route("/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def delete_comment( comment_id ):

    existing_comment = CommentModel.query.get(comment_id)

    if not existing_comment:
      return {"message": "comment not found"}, HTTPStatus.NOT_FOUND

    if not g.current_user.id == existing_comment.user_id:
      return {"message": "Not your movie, hands off!"}, HTTPStatus.UNAUTHORIZED

    try:
        existing_comment.remove()

    except ValidationError as e:
        return {"errors:": e.messages, "messages": "Something went wrong"}

    return comment_schema.jsonify(existing_comment), HTTPStatus.OK


@router.route("/books/<int:book_id>/comments", methods=["POST"])
@secure_route
def create_comment(book_id):

  comment_dictionary = request.json
  try:
    comment = comment_schema.load(comment_dictionary)

  except ValidationError as e:
    return { "errors": e.messages, "message": "Something went wrong" }

  comment.book_id = book_id
  comment.user_id = g.current_user.id
  comment.save()

  return comment_schema.jsonify(comment), HTTPStatus.CREATED


@router.route("/books/<int:book_id>/comments/<int:comment_id>", methods=["PUT"])
@secure_route
def update_comment(book_id, comment_id):
    comment_dictionary = request.json
    existing_comment = CommentModel.query.filter_by(id=comment_id).first()

    if not existing_comment:
      return {"message": "comment not found"}, HTTPStatus.NOT_FOUND

    if not g.current_user.id == existing_comment.user_id:
      return {"message": "Not your comment, hands off!"}, HTTPStatus.UNAUTHORIZED
    try:
        existing_comment.content = comment_dictionary['content']
        existing_comment.save()


    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }

    return comment_schema.jsonify(existing_comment), HTTPStatus.OK

