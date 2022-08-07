

from app import ma
from models.authors import AuthorModel

class AuthorSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = AuthorModel
    load_instance = True
    exclude = ("created_at", "updated_at")