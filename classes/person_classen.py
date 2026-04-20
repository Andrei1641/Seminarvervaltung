from abc import ABC, abstractmethod

from classes.data_time import DateTim
from factories.date_time_factory import DateTimeFactory
from interfaces.nameable import Nameable
from interfaces.serializable import Serializable


class Person(ABC):
    def __init__(self, first_name: str, second_name: str, email_address: str):
        self._first_name: str = first_name
        self._second_name: str = second_name
        self._email_address: str = email_address
        self._booked_time: list[tuple[DateTim, DateTim, str]] = []                #(start_time, end_time, course_name)


    # def deserialize_booked_time(self, old_booked_time: list[tuple[str, str, str]]):         # !only sorted!
    #     for i in old_booked_time:
    #         start: DateTim = DateTimeFactory.create_date_time(i[0])
    #         end: DateTim = DateTimeFactory.create_date_time(i[1])
    #         self._booked_time.append((start, end, i[2]))

    def _find_time(self, start_time: DateTim, end_time: DateTim):
        time = (start_time, end_time)

        l = 0
        r = len(self._booked_time) - 1
        mid = -1

        while l <= r:
            mid = (l + r) // 2
            guess_time = self._booked_time[mid]

            if time[0] < guess_time[0] and time[1] < guess_time[0]:
                r = mid - 1
            elif time[0] > guess_time[1] and time[1] > guess_time[1]:
                l = mid + 1
            else:
                return mid, 0
        return mid, 1

    def free_up_time(self, time_room):
        place, state = self._find_time(time_room[0], time_room[1])
        if not state:
            self._booked_time.pop(place)

    def book_time(self, start_time: DateTim, end_time: DateTim, course_name: str):
        place, state = self._find_time(start_time, end_time)

        if place == -1:
            self._booked_time.append((start_time, end_time, course_name))
        elif state:
            self._booked_time.insert(place, (start_time, end_time, course_name))
        else:
            raise ValueError(f'this person is already on course: {self._booked_time[place][2]}')


    def get_name(self) -> str:
        return self._second_name + ' ' + self._first_name


    def _base_str(self) -> str:
        name: str = f'Name: {self._first_name} {self._second_name}'
        email: str = f'Email-Adresse: {self._email_address}'
        return f'{name}\n{email}\n'


    def get_dict(self) -> dict:
        # serialized__booked_time: list[tuple] = []
        # if self._booked_time:
        #     for i in self._booked_time:
        #         serialized__booked_time.append((str(i[0]), str(i[1]), i[2]))

        d: dict = {
                                self.get_name() : {
                                                    'first name' : self._first_name,
                                                    'second name' : self._second_name,
                                                    'email address' : self._email_address,
                                                    # 'booked time' : serialized__booked_time
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
        docent_dict[self.get_name()]['theme'] = self.__list_an_themes

        return docent_dict


class Participant(Person, Nameable, Serializable):
    def __str__(self) -> str:
        base_str = self._base_str()
        role: str = f'Rolle: Teilnehmer'
        return f'{base_str}{role}\n'
