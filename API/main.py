from Endpoints.routes import routers
from fastapi import FastAPI
from Infrastructure.Container.container import Container
from Infrastructure.Utils.singleton import singleton
from Infrastructure.Configuration.project_configuration import ProjectConfiguration


@singleton
class AppCreator:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=ProjectConfiguration.PROJECT_NAME,
            version="0.0.1",
        )

        # set db and container
        self.container = Container()
        self.db = self.container.db()

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(
            routers, prefix=ProjectConfiguration.API_PREFIX)


app_creator = AppCreator()
app = app_creator.app
