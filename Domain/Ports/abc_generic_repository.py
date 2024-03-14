from abc import ABC, abstractmethod


class AbcGenericRepository(ABC):

    @abstractmethod
    def read_by_options(self, schema, eager=False):
        pass


    @abstractmethod
    def read_by_id(self, id: int, eager=False):
        pass


    @abstractmethod
    def add(self, schema):
        pass


    @abstractmethod
    def update(self, id: int, schema):
        pass


    @abstractmethod
    def delete_by_id(self, id: int):
        pass
