from abc import ABC, abstractmethod

from interfaces.callable import Nameable
from interfaces.serializable import Serializable


class Person(ABC):
    def __init__(self, first_name: str, second_name: str, email_address: str):
        self._first_name: str = first_name
        self._second_name: str = second_name
        self._email_address: str = email_address


    def get_name(self) -> str:
        return self._second_name + ' ' + self._first_name


    def _base_str(self) -> str:
        name: str = f'Name: {self._first_name} {self._second_name}'
        email: str = f'Email-Adresse: {self._email_address}'
        return f'{name}\n{email}\n'


    def get_dict(self) -> dict:
        d: dict = {
                                self.get_name() : {
                                                    'first name' : self._first_name,
                                                    'second name' : self._second_name,
                                                    'email address' : self._email_address,
                                                  }
                             }
        return d



    @abstractmethod
    def __str__(self) -> str:
        ...

class Docent(Person, Nameable, Serializable):

    def __init__(self, first_name: str, second_name: str, email_adresse: str, list_an_themes: list[str]):
        super().__init__(first_name, second_name, email_adresse)
        self.__list_an_themes: list[str] = list_an_themes

    def __str__(self) -> str:
        base_str = self._base_str()
        role: str = f'Rolle: Dozent'
        t = ", ".join(self.__list_an_themes)
        theme: str = f'Themen: {t}'

        return f'{base_str}{role}\n{theme}\n'


    def get_dict(self) -> dict:
        docent_dict = super().get_dict()
        docent_dict[self.get_name()] = {'theme' : self.__list_an_themes}

        return docent_dict


class Participant(Person, Nameable, Serializable):
    def __str__(self) -> str:
        base_str = self._base_str()
        role: str = f'Rolle: Teilnehmer'
        return f'{base_str}{role}\n'
