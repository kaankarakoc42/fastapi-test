#fastapi and jwt auth
from fastapi import APIRouter,Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from .Token import *
from .models import *

#database stufs
from sqlalchemy import and_

router = APIRouter(
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/users")
def getUsers(db = Depends(get_db)):
    return db.query().with_entities(Users.username,Users.id).all()

@router.get("/users/me")
def profile(user:UsersModel = Depends(getCurrentActifUser)):
    print("user :"+user.username)
    return user

@router.post("/login")
def login(user:OAuth2PasswordRequestForm =Depends()):
    return createToken(user)
     
    

@router.post("/register")
def register(user:UsersModel,db = Depends(get_db)):
    new_user = Users(**jsonable_encoder(user))
    new_user.password = Hash.hash(new_user.password)
    if not db.query(Users).filter(Users.username==new_user.username).first():
       db.add(new_user)
       db.commit()
       return {"state":"ok"}
    return {"state":"error"}

