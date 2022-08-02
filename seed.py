
#Difference from express: Our seed file, needs to know about flask (app) and SQL Alchemy (db)

from app import app, db
from models.data import  users_list, authors_list , book_condition_list , type_list,  genre_list , books_list, book_listing_list, comment_list

with app.app_context():
    
  try:
    print("Recreating DB")
    db.drop_all() #removing eberything from the db
    db.create_all() #This will create the tables in the db

    print("seeding our database")

    db.session.add_all(users_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit

    db.session.add_all(authors_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit

    db.session.add_all(book_condition_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit

    db.session.add_all(type_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit


    db.session.add_all(genre_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit


    db.session.add_all(books_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit


    db.session.add_all(book_listing_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit

    db.session.add_all(comment_list) #provides session object that will add a list of things to the db
    db.session.commit() #like github add, commit

  except Exception as e:
    print(e)