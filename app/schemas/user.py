#app/schemas/user.py

from pydantic import BaseModel, EmailStr, constr
from datetime import datetime

class UserBase(BaseModel):
    email : EmailStr
    username : constr(min_length=3, max_length=50)

class UserCreate(UserBase):
    password : constr(min_length=4, max_length=50)

class UserOut(UserBase):
    id : int
    role : str
    created_at : datetime

    model_config = {"from_attributes":True}
