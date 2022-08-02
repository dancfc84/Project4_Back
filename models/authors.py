from app import db, ma
from models.base import BaseModel

class AuthorModel(db.Model, BaseModel):
    
    __tablename__ = "authors"

    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
