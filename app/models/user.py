#app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True, index=True)
    email = Column(String(255),unique=True, index=True, nullable=False)
    username = Column(String(50),unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default='user')   #user, admin
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    posts = relationship("Post", back_populates="author", cascade="all,delete-orphan")
    comments = relationship("Comment", back_populates="author", cascade="all,delete-orphan")

