from app import db, ma
from models.base import BaseModel

class BookTypeModel(db.Model, BaseModel):
    
    __tablename__ = "book_types"

    type = db.Column(db.Text, nullable=False, unique=True)

