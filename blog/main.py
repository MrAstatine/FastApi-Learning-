from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Response, status, HTTPException
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


# @app.post("/blog", status_code=201)
@app.post("/blog", status_code=status.HTTP_201_CREATED)
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


@app.get("/blog")
def all(db: Session = Depends(get_db)):
    blogs = db.query(
        models.Blog
    ).all()  # this returns all the data from the table that have model as Blog
    return blogs


@app.get("/blog/{id}", status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = (
        db.query(models.Blog).filter(models.Blog.id == id).first()
    )  # here v r filtering the data to get only the one with matching id
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with id {id} does not exsist"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with given ID {id} does not exist",
        )
    return blog
