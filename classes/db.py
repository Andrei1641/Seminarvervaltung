from types import NoneType
from interfaces.nameable import Nameable

from classes.person_classen import *

class DataBase:
    def __init__(self, t: type):
        self.__db: dict[str, Nameable] = {}
        self.__type: type = t

    def __len__(self) -> int:
        return len(self.__db)

    def insert_in_db(self, obj: Nameable):
        self.__db[obj.get_name()] = obj


    def pop(self, name: str):
        self.__db.pop(name, None)

    def get_type(self) -> type:
        return type(self.__type)

    def get(self, name):
        return self.__db.get(name, 0)

    def get_names(self) -> str:
        return ', '.join(self.__db)