from dataclasses import dataclass
from app import db


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(128),  nullable=False, unique=True)
    password: str = db.Column(db.String(128),  nullable=False)

