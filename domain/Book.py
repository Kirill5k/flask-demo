from dataclasses import dataclass


@dataclass
class Book:
    isbn: int
    name: str
    price: float
