from fastapi import FastAPI
from .routes import users
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.include_router(users.router)

