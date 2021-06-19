from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.exceptions import HTTPException
from .hashing import Hash
#database stufs
from .database import get_db,localSession
from .database.schemas import *
from sqlalchemy import and_


expiration_time = 30

db = localSession()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def authUser(username,password):
    user=db.query(Users).filter(Users.username==username).first()
    if not user: return None
    if Hash.verify(password,user.password):
       return user
    return None
       
async def getCurrentActifUser(token = Depends(oauth2_scheme)): 
    try:
      decoded_token=Hash.decodeJWT(token)
    except:
      raise HTTPException(HTTP_401_UNAUTHORIZED,"Could not validate credentials")
    return db.query(Users).filter(Users.username==decoded_token["sub"]).first()
