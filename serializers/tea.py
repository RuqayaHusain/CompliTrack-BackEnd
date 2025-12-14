from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema

class TeaSchema(BaseModel):
  id: Optional[int] = True # This makes sure you don't have to explicitly add an id when sending json data
  name: str
  in_stock: bool
  rating: int
  comments: List[CommentSchema] = []

  class Config:
    orm_mode = True
