from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship  # Import the relationship function from SQLAlchemy ORM
from .base import BaseModel  # Import the base model for SQLAlchemy
from .comment import CommentModel  # Import the CommentModel class for establishing relationships

# Inherits from BaseModel, a custom base class that extends SQLAlchemy's Base
class TeaModel(BaseModel):

    __tablename__ = "teas"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Tea Table.
    name = Column(String, unique=True)
    in_stock = Column(Boolean)
    rating = Column(Integer)

    # Define a relationship with the CommentModel table
    comments = relationship("CommentModel", back_populates="tea")