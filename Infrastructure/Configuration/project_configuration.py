from pydantic import BaseSettings


class project_configuration(BaseSettings):
    PROJECT_NAME: str = "Agro Smart Weather Forecast Api"
    API_PREFIX: str = "/api"

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    PAGE = 1
    PAGE_SIZE = 20
    ORDERING = "-id"
