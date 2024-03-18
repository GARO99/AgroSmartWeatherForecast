from dependency_injector import containers, providers
from Domain.Ports.abc_generic_repository import AbcGenericRepository
from Infrastructure.Adapters.sqlalchemy_generic_repository import SqlAlchemyGenericRepository
from Infrastructure.Configuration.project_configuration import ProjectConfiguration
from Infrastructure.Context.persistence_context import PersistenceContext


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "Domain"
        ]
    )
    
    db = providers.Singleton(
        PersistenceContext, 
        db_url=ProjectConfiguration().DATABASE_URI
    )
    
    generic_repository = providers.Factory(
        SqlAlchemyGenericRepository,
        session_factory= db.provided.session,
        model=AbcGenericRepository
    )