from Endpoints.routes import routers
from fastapi import FastAPI
from Infrastructure.Utils.singleton import singleton
from Infrastructure.Configuration.project_configuration import project_configuration


@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=project_configuration.PROJECT_NAME,
            version="0.0.1",
        )

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(
            routers, prefix=project_configuration.API_PREFIX)


app_creator = AppCreator()
app = app_creator.app