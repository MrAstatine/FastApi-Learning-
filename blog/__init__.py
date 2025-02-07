from fastapi import FastAPI

app = FastAPI()


@app.get("/blog")
def create():
    return "creating"
