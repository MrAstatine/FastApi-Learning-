from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = (
    "sqlite:///./blog.db"  # SQLite URL to local file if you're not using a real DB
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# till here v have created the engine. now v start mapping

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# now v create session

from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
