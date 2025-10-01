#app/crud/post.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models
from app.schemas.post import PostCreate

def get_by_id(db : Session, post_id : int):
    return db.get(models.post.Post, post_id)

def list_post(db : Session):
    return db.query(models.post.Post).order_by(models.post.Post.id.desc()).all()

def create(db : Session, data : PostCreate):
    #validar author
    author = db.get(models.user.User, data.author_id)
    if not author:
        raise HTTPException(status_code=404, detail='autor no existe')

    post = models.post.Post(
        title = data.tittle,
        content = data.content,
        author_id = data.author_id
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def delete(db : Session, post_id : int):
    post = get_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail='correo no encontrado')
    db.delete(post)
    db.commit()



