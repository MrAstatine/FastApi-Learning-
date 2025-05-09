# imported for changing port number
# import uvicorn
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "blog list"}


@app.get("/about")
def about():
    return {"data": "about page"}


@app.get("/blog")
def some_blog(limit=6, published: bool = False, sort: Optional[str] = None):
    # published u get here is string. so typecast into boolean for if else statement to work
    # only gets 10 published blogs
    if published:
        return {"data": f"{limit} published blogs from the db list"}
    else:
        return {"data": f"{limit} unpublished blogs from the db list"}


# if u keep this after /blog/{id} route then here unpublished will b consisderd as a parameter. so just put it up to as it employs dynamic routing
@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blkogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]  # this category is optional


@app.post("/blog")
def create_blog(blog: Blog):
    # return request
    return {"data": f"blog created with title as {blog.title}"}


"""
# this is to change the port. for this u import uvicorn
to get in port 9300 u run python3 main.py
otherwise when u run uvicorn main:app --reload it runs on 8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9300)
"""
