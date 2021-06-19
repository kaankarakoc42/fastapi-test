from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.sql.expression import null
from .database import Base
from datetime import datetime

class Articles(Base):
      __tablename__ = "articles"
      id = Column("id",Integer,autoincrement=True,primary_key=True)
      author =  Column("author",String)
      title = Column("title",String)
      content = Column("content",String)
      date = Column("date",DateTime,default=datetime.now())


class Users(Base):
      __tablename__ = "users"
      id = Column("id",Integer,autoincrement=True,primary_key=True)
      username = Column("username",String,nullable=False)
      password = Column("password",String,nullable=False)
      email = Column("email",String,nullable=False)
      date = Column("date",DateTime,default=datetime.now()) 

Base.metadata.create_all()