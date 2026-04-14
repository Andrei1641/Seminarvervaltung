from types import NoneType
from interfaces.nameable import Nameable

from classes.person_classen import *

class DataBase:
    def __init__(self) -> None:
        self.__db: dict[str, Nameable] = {}

    def __len__(self) -> int:
        return len(self.__db)

    def insert_in_db(self, obj: Nameable):
        if isinstance(obj, self.get_type()) or self.get_type() == NoneType:
            self.__db[obj.get_name()] = obj
        else:
            raise ValueError(f'this data base not for this type: {type(obj)}')

    def pop(self, name: str):
        self.__db.pop(name, None)

    def get_type(self) -> type:
        first_value = next(iter(self.__db.values()), None)
        return type(first_value)

    def get(self, name):
        return self.__db.get(name, 0)

    def get_names(self) -> str:
        return ', '.join(self.__db)