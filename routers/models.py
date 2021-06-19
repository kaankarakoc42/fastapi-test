from pydantic import BaseModel

class ArticlesModel(BaseModel):
      title:str
      content:str

class UsersModel(BaseModel):
      username:str
      password:str
      email:str
      
      
