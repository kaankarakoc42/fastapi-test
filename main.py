from fastapi import FastAPI
from routers import articles,users
import sys
sys.path.append("..")

app = FastAPI()

app.include_router(articles.router)
app.include_router(users.router)