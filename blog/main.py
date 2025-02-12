from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from . import schemas, models
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(engine)

"""
@app.post("/blog")
def create(request: schemas.Blog):
    return request
"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog")
def create(
    request: schemas.Blog, db: Session = Depends(get_db)
):  # by typing Depends v r creating this session into a pydantic thing
    # return db
    new_blog = models.Blog(title=request.title, body=request.body)
    # these below 3 steps r imp to insert data into db
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
