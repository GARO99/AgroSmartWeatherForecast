import os
from dotenv import load_dotenv
from pydantic import BaseSettings

env_path = '../../.env'

load_dotenv(dotenv_path=env_path)

class ProjectConfiguration(BaseSettings):
    # base
    PROJECT_NAME: str = "Agro Smart Weather Forecast Api"
    API_PREFIX: str = "/api"

    # database
    DB_HOST: str = os.getenv("DB_HOST")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_ENGINE: str = os.getenv("DB_ENGINE")
    DB_NAME: str = os.getenv("DB_NAME")

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI = DATABASE_URI_FORMAT.format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )
