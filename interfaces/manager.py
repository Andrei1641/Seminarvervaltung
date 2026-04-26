from abc import ABC, abstractmethod

from classes.db import DataBase
from interfaces.serializable import Serializable



class Manager(ABC):

    @staticmethod
    def db_get_objects(db: DataBase) -> list[Serializable]:
        all_names = db.get_names()
        all_names = all_names.split(', ')
        all_ob: list[Serializable] = []

        for i in all_names:
            all_ob.append(db.get(i))

        return all_ob

    @staticmethod
    def _get_d(db: DataBase, name: str):
        all_objects: list[Serializable] = Manager.db_get_objects(db)

        d: dict = {f'all {name}': {}}

        if all_objects != [0]:
            for i in all_objects:
                d[f'all {name}'].update(i.get_dict())
        else:
            d[f'all {name}'] = ''

        return d


    @abstractmethod
    def get_type(self) -> type:
        ...

    @abstractmethod
    def get_dict(self) -> dict:
        ...

    @abstractmethod
    def find_func(self, *args):
        ...