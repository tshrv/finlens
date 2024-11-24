from faker import Faker
from fastapi import Depends, FastAPI
from loguru import logger
from sqlalchemy.orm import Session
from src.dependencies import get_db_session
from src.models import User

fake = Faker("en_US")
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI boilerplate!"}


@app.get("/users")
def read_users(session: Session = Depends(get_db_session)):
    data = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
    }
    logger.debug(data)

    return session.query(User).all()
