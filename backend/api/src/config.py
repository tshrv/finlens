from decouple import config
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = config("DATABASE_URL")
    SECRET_KEY: str = config("SECRET_KEY")

    class Config:
        env_file = ".env"


settings = Settings()
