import os
from typing import List
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_path = '../../.env'

load_dotenv(dotenv_path=env_path)

class ProjectConfiguration(BaseSettings):
    # database
    __DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"
    __DB_HOST: str = os.getenv("DB_HOST")
    __DB_USER: str = os.getenv("DB_USER")
    __DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    __DB_PORT: str = os.getenv("DB_PORT")
    __DB_ENGINE: str = os.getenv("DB_ENGINE")
    __DB_NAME: str = os.getenv("DB_NAME")


    # base
    @staticmethod
    def PROJECT_NAME() -> str:
        return "Agro Smart Weather Forecast Api"


    @staticmethod
    def API_PREFIX() -> str:
        return "/api"

    # CORS
    @staticmethod
    def BACKEND_CORS_ORIGINS() -> List[str]:
        return ["*"]

    @property
    def DATABASE_URI(self) -> str:
        print(self.__DB_USER)
        return self.__DATABASE_URI_FORMAT.format(
            db_engine=self.__DB_ENGINE,
            user=self.__DB_USER,
            password=self.__DB_PASSWORD,
            host=self.__DB_HOST,
            port=self.__DB_PORT,
            database=self.__DB_NAME,
        )
