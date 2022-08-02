from app import db

# ! Now I'm going to make a join table, using SQLAlchemy!
book_sale = db.Table('book_sale',
    # ! Here we define our 2 columns, just like in SQL.
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('book_listings_id', db.Integer, db.ForeignKey('book_listings.id'), primary_key=True)
)


