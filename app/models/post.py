#app/models/post.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func, null
from sqlalchemy.orm import relationship
from app.database import Base

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all,delete-orphan")

