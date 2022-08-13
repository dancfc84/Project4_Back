from app import db, ma
from models.base import BaseModel
from models.users import UserModel
from models.authors import AuthorModel
from models.genres import GenreModel
from models.book_sale import book_sale
from models.book_wishlist import book_wishlist

class BookModel(db.Model, BaseModel):
    
    __tablename__ = "books"

    name = db.Column(db.Text, nullable=False, unique=True)
    year_released = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer)
    pages = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)

    #Add relationships
    listing = db.relationship('BookListingModel', backref='book_listings', secondary=book_sale) #This allows us to make a join table
    wishlist = db.relationship('UserModel', backref='book_wishlists', secondary=book_wishlist) #This allows us to make a join table
    user = db.relationship("UserModel", backref="book_users")
    genre = db.relationship("GenreModel", backref="book_genre")
    author = db.relationship("AuthorModel", backref="book_author")

