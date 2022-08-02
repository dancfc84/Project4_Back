from app import ma
from models.book_listing import BookListingModel

class BookListingSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = BookListingModel
    load_instance = True
    # By default the auto-generated schemas exclude foreign key fields, add line below for you do be able to access them:
    include_fk = True