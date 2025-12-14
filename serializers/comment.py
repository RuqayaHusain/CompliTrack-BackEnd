from pydantic import BaseModel

class CommentSchema(BaseModel):
  id: int
  content: str

  class Config:
    orm_mode = True
