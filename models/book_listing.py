from app import db
from models.base import BaseModel
from models.book_type import BookTypeModel
from models.book_condition import BookConditionModel


class BookListingModel(db.Model, BaseModel):

    __tablename__ = "book_listings"

    type_id = db.Column(db.Integer, db.ForeignKey("book_types.id", ondelete="CASCADE"), nullable=False)
    condition_id = db.Column(db.Integer, db.ForeignKey("book_conditions.id", ondelete="CASCADE"), nullable=False)
    #Look into why this can't be nullable
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))

    user = db.relationship("UserModel", backref="book_listing_users")
    type = db.relationship("BookTypeModel", backref="book_listing_type")
    condition = db.relationship("BookConditionModel", backref="book_listing_condition")
    

