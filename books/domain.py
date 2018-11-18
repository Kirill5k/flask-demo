from datetime import datetime
from dataclasses import dataclass
from dataclasses import asdict
from app import db


@dataclass
class Book(db.Model):
    __tablename__ = 'books'

    id: int = db.Column(db.Integer, primary_key=True)
    isbn: int = db.Column(db.Integer, nullable=False, unique=True)
    name: str = db.Column(db.String(128),  nullable=False)
    price: float = db.Column(db.Float,  nullable=False)
    date_added: datetime = db.Column(db.DateTime,  default=db.func.current_timestamp())

    def to_dict(self):
        return asdict(self)
