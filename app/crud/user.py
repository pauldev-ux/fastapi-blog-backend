#app/crud/user.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import  IntegrityError
from fastapi import HTTPException, status
from app import models
from app.schemas.user import UserCreate
from app.utils.security import hash_password

def get_by_id(db : Session, user_id : int):
    return db.get(models.user.User, user_id)

def get_by_email(db : Session, email : str):
    return db.query(models.user.User).filter(models.user.User.email == email).first()

def get_by_username(db : Session, username : str):
    return db.query(models.user.User).filter(models.user.User.username == username).first()

def list_users(db : Session):
    return db.query(models.user.User).all()

def create(db : Session, data : UserCreate):
    user = models.user.User(
        email = data.email,
        username = data.username,
        hash_password = hash_password(data.password),
        role = 'user',
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email o username ya existen")
    db.refresh(user)
    return user


def delete(db : Session, user_id : int):
    user = get_by_id(db, user_id)
    if not user :
        raise HTTPException(status_code=404, detail="usuarios no encontrado")
    db.delete(user)
    db.commit()

