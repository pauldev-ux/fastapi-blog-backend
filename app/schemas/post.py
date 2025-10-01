#app/schemas/post.py
from pydantic import BaseModel, constr
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    tittle : constr(min_length=1, max_length=500)
    content : str

class PostCreate(PostBase):
    author_id : int

class PostOut(PostBase):
    id : int
    author_id : int
    created_at : datetime
    update_at : Optional[datetime] = None

    model_config = {"from_attributes":True}

