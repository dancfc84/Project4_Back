from app import db
from models.base import BaseModel
from models.users import UserModel

class CommentModel(db.Model, BaseModel):

    __tablename__ = "comments"

    #Conrehnt of the comment
    content = db.Column(db.Text, nullable=False)
    # You give it the primary key of the movies table
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))

    # This line is for serialization. Tells our comment about our Movie model.
    # Assosciates 2 models together. Only required if using foreign key one to many relationship
    # It won't make a new column, but instead, specifies a relationship between
    # 2 models.
    # ? backref should be the table name of this current table.
    book = db.relationship("BookModel", backref="comment_user")

