from app import ma
from models.book_condition import BookConditionModel

class BookConditionSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = BookConditionModel
    load_instance = True