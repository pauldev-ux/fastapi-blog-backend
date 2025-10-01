from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user, post, comment

app = FastAPI(title='Blog con FastAPI')

@app.get('/')
def root():
    return {"message": "Blog API funcionando"}

@app.get('startup')
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix='/users', tags=['users'])
app.include_router(post.router, prefix='/posts', tags=['post'])
app.include_router(comment.router, prefix='/comment', tags=['comments'])