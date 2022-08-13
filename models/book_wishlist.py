from app import db

# ! Now I'm going to make a join table, using SQLAlchemy!
book_wishlist = db.Table('book_wishlist',
    # ! Here we define our 2 columns, just like in SQL.
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

