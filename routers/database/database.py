#! usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#creating engine and session maker
engine = create_engine("sqlite:///mydatabase.db",connect_args={"check_same_thread":False})
localSession=sessionmaker(bind=engine,autocommit=False,autoflush=False)

#base binding to engine
Base = declarative_base()
Base.metadata.bind = engine


async def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()
