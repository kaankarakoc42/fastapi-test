from .hashing import Hash
from datetime import datetime, timedelta
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.exceptions import HTTPException
from .Oauth2 import *

expiration_time = 30

def createToken(data:dict):
    user = authUser(data.username,data.password)
    print(data,user.username)
    if not user: raise HTTPException(HTTP_401_UNAUTHORIZED,"invalid username or password")
    token = Hash.encodeJWT({"sub":data.username,"exp":datetime.utcnow()+timedelta(minutes=expiration_time)})
    print(token)
    return {"access_token":token,"token_type":"Bearer"}