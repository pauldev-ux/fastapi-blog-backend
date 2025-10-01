#app/routers/comment.py

from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.comment import CommentCreate, CommentOut
from app.crud import comment as comment_crud

router = APIRouter()

@router.post("/", response_model=CommentOut, status_code=status.HTTP_201_CREATED)
def create_comment(payload: CommentCreate, db: Session = Depends(get_db)):
    return comment_crud.create(db, payload)

@router.get("/post/{post_id}", response_model=List[CommentOut])
def list_comments_by_post(post_id: int, db: Session = Depends(get_db)):
    return comment_crud.list_by_post(db, post_id)

@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment_crud.delete(db, comment_id)
    return
