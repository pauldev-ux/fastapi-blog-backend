#app/schemas/comment.py

from pydantic import BaseModel, constr
from datetime import  datetime

class CommentBase(BaseModel):
    content : constr(min_length=1)

class CommentCreate(CommentBase):
    author_id : int
    post_id : int

class CommentOut(CommentBase):
    id : int
    author_id : int
    post_id : int
    created_at : datetime

    model_config = {"from_attributes":True}



