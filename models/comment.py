from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class CommentModel(BaseModel):

    __tablename__ = "comments"  # The name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the comment
    content = Column(String, nullable=False)  # The text content of the comment

    # ForeignKey establishes a connection to the teas table
    tea_id = Column(Integer, ForeignKey('teas.id'), nullable=False)
    tea = relationship("TeaModel", back_populates="comments")  # Defines the relationship to the TeaModel
