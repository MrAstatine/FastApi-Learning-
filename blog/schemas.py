from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(BaseModel):
    title: str  # the field with str or something is only going to b shown

    class Config:
        orm_mode = True  # this needs to b added


class User(BaseModel):
    name: str
    email: str
    password: str
