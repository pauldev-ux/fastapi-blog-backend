#app/routers/user.py
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session
from websockets.legacy.server import HTTPResponse

from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud import user as user_crud

router = APIRouter()

@router.post('/', response_model= UserOut, status_code=status.HTTP_201_CREATED)
def create_user(new : UserCreate, db : Session = Depends(get_db)):
    return user_crud.create(db, new)

@router.get('/', response_model=list[UserOut])
def list_users(db : Session = Depends(get_db)):
    return user_crud.list_users(db)

@router.get('/{user_id}', response_model=UserOut)
def get_user(user_id : int, db : Session = Depends(get_db)):
    user = user_crud.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='usuario no encontrado')
    return user

@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(user_id : int, db : Session = Depends(get_db)):
    user_crud.delete(db, user_id)
    return




