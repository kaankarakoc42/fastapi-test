from fastapi import APIRouter,Depends
from fastapi.encoders import jsonable_encoder
#database
from sqlalchemy import and_
from .models import ArticlesModel
#jwt token
from .Token import *


router = APIRouter(
    prefix="/articles",
    tags=["articles"],
    responses={404: {"description": "Not found"}},
)

@router.get("/articles")
def index(db=Depends(get_db)):
    return db.query(Articles).all()

@router.post("/addarticle")
def getarticles(article:ArticlesModel,db=Depends(get_db),user=Depends(getCurrentActifUser)):
    kwargs = jsonable_encoder(article)
    kwargs["author"]=user.username
    new_Article = Articles(**kwargs)
    db.add(new_Article)
    db.commit()
    return kwargs

@router.post("/deletearticle/{id}")
def deleteArticle(id:int,db=Depends(get_db),user=Depends(getCurrentActifUser)):
    query = db.query(Articles).filter(and_(Articles.id==id,Articles,Articles.username == user.username))
    if query.first():
       query.delete()
       db.commit()
       return {"state":"ok"}
    return {"state":"error","message":"no result matched"}

@router.get("/article/{id}")
async def read_items(id:int,db=Depends(get_db)):
      result = db.query(Articles).filter(id==Articles.id)
      return result.first()