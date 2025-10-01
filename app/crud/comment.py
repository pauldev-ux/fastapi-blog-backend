#app/crud/comment.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models
from app.schemas.comment import CommentCreate

def get_by_id(db : Session, comment_id : int):
    return db.get(models.comment.Comment, comment_id)

def list_by_post(db : Session, post_id : int):
    return (
        db.query(models.comment.Comment)
        .filter(models.comment.Comment.post_id == post_id)
        .order_by(models.comment.Comment.id.desc()).all()
    )

def create(db : Session, data : CommentCreate):
    #validar relaciones
    author = db.get(models.user.User, data.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Autor no existe")
    post = db.query(models.post.Post).get(data.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Correo no existe")

    comment = models.comment.Comment(
        content = data.content,
        author_id = data.author_id,
        post_id = data.post_id
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def delete(db : Session, comment_id : int):
    comment = get_by_id(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail='comentario no encontrado')
    db.delete(comment)
    db.commit()
