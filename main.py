from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "blog list"}


@app.get("/about")
def about():
    return {"data": "about page"}


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
