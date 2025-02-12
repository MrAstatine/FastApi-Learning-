from .database import Base
from sqlalchemy import Column, Integer, String


class Blog(Base):
    __tablename__ = "blogs"  # name of the table in the database
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
