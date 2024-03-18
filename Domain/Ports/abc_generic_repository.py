from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from Domain.Entities.Base.base_entity import BaseEntity

Entity = TypeVar("Entity", bound=BaseEntity)

class AbcGenericRepository(ABC, Generic[Entity]):

    @abstractmethod
    def read_by_options(self, entity: type[Entity], eager=False):
        pass


    @abstractmethod
    def read_by_id(self, id: int, eager=False):
        pass


    @abstractmethod
    def add(self, entity: type[Entity]):
        pass


    @abstractmethod
    def update(self, id: int, entity: type[Entity]):
        pass


    @abstractmethod
    def delete_by_id(self, id: int):
        pass
