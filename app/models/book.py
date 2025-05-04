from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Book(db.Model): # gonna take this Book model it is gonna be a books table in  my database
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            description=data["description"]
        )
    # my_book = Book.from_dict(book_data)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description":self.description
        }
