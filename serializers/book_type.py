from app import ma
from models.book_type import BookTypeModel

class BookTypeSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = BookTypeModel
    load_instance = True