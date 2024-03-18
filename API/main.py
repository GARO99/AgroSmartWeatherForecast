from Endpoints.routes import routers
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
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

        # set cors
        if ProjectConfiguration.BACKEND_CORS_ORIGINS:
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in ProjectConfiguration.BACKEND_CORS_ORIGINS],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"

        self.app.include_router(
            routers, prefix=ProjectConfiguration.API_PREFIX)


app_creator = AppCreator()
app = app_creator.app
db = app_creator.db
container = app_creator.container
