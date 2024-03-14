from contextlib import AbstractContextManager
from Domain.Exceptions.duplicated_error_exception import DuplicatedErrorException
from Domain.Exceptions.not_found_error_exception import NotFoundErrorException
from Domain.Ports.abc_generic_repository import AbcGenericRepository
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload
from typing import Callable

from Infrastructure.Configuration.project_configuration import project_configuration
from Infrastructure.Utils.sqlalchemy_query_builder import dict_to_sqlalchemy_filter_options


class SqlAlchemyGenericRepository(AbcGenericRepository):
    
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], model) -> None:
        self.session_factory = session_factory
        self.model = model


    def read_by_options(self, schema, eager_loading=False):
        with self.session_factory() as session:
            schema_as_dict = schema.dict(exclude_none=True)
            ordering = schema_as_dict.get("ordering", project_configuration.ORDERING)
            order_query = (
                getattr(self.model, ordering[1:]).desc()
                if ordering.startswith("-")
                else getattr(self.model, ordering).asc()
            )
            page = schema_as_dict.get("page", project_configuration.PAGE)
            page_size = schema_as_dict.get("page_size", project_configuration.PAGE_SIZE)
            filter_options = dict_to_sqlalchemy_filter_options(self.model, schema.dict(exclude_none=True))
            query = session.query(self.model)
            if eager_loading:
                for eager_loading in getattr(self.model, "eagers", []):
                    query = query.options(joinedload(getattr(self.model, eager_loading)))
            filtered_query = query.filter(filter_options)
            query = filtered_query.order_by(order_query)
            if page_size == "all":
                query = query.all()
            else:
                query = query.limit(page_size).offset((page - 1) * page_size).all()
            total_count = filtered_query.count()
            return {
                "founds": query,
                "search_options": {
                    "page": page,
                    "page_size": page_size,
                    "ordering": ordering,
                    "total_count": total_count,
                },
            }


    def read_by_id(self, id: int, eager_loading=False):
        with self.session_factory() as session:
            query = session.query(self.model)
            if eager_loading:
                for eager_loading in getattr(self.model, "eagers", []):
                    query = query.options(joinedload(getattr(self.model, eager_loading)))
            query = query.filter(self.model.id == id).first()
            if not query:
                raise NotFoundErrorException(detail=f"not found id : {id}")
            return query


    def create(self, schema):
        with self.session_factory() as session:
            query = self.model(**schema.dict())
            try:
                session.add(query)
                session.commit()
                session.refresh(query)
            except IntegrityError as e:
                raise DuplicatedErrorException(detail=str(e.orig))
            return query


    def update(self, id: int, schema):
        with self.session_factory() as session:
            session.query(self.model).filter(self.model.id == id).update(schema.dict(exclude_none=True))
            session.commit()
            return self.read_by_id(id)

