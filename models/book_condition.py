from app import db, ma
from models.base import BaseModel

class BookConditionModel(db.Model, BaseModel):
    
    __tablename__ = "book_conditions"

    condition = db.Column(db.Text, nullable=False, unique=True)

