#app/routers/post.py
from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.post import PostCreate, PostOut
from app.crud import post as post_crud

router = APIRouter()

@router.get('/', response_model=List[PostOut])
def list_post(db : Session = Depends(get_db)):
    return post_crud.list_post(db)

@router.get('/', response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(new : PostCreate, db : Session = Depends(get_db)):
    return post_crud.create(db, new)

@router.get('/{post_id}', response_model=PostOut)
def get_post(post_id : int, db : Session = Depends(get_db)):
    post = post_crud.get_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")
    return post

@router.delete('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post_crud.delete(db, post_id)
    return


