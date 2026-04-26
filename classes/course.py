import copy
from classes.data_time import DateTim

from classes.db import DataBase
from classes.person_classen import Docent, Participant
from interfaces.nameable import Nameable
from interfaces.serializable import Serializable


class Course(Nameable, Serializable):
    def __init__(self, title: str, date: DateTim, duration: int, place: str, persons: dict[str, list[str]], max_count: dict[str, int]):
        self.__title: str = title
        self.__date: DateTim = date
        self.__duration: int = duration      #minute
        self.__place: str = place
        self.__persons: dict[str, list[str]] = persons
        self.__max_counts: dict[str, int] = max_count
        self.__time_room: tuple[DateTim, DateTim] = self.adjust_time_room()

    def get_persons_t(self):
        return self.__persons.keys()

    def get_time_room(self) -> tuple[DateTim, DateTim]:
        return self.__time_room

    def adjust_time_room(self) -> tuple[DateTim, DateTim]:

        course_start = self.__date

        course_end = copy.copy(self.__date)
        course_end.add_time(minutes=self.__duration)

        return course_start, course_end

    def get_dict(self) -> dict[str, dict]:


        course_dict: dict = {
                                self.get_name(): {
                                                    'course info' : {
                                                                        'title' : self.__title,
                                                                        'date' : str(self.__date),
                                                                        'duration' : self.__duration,
                                                                        'max participant count' : self.__max_counts['participant'],
                                                                        'place' : self.__place
                                                                    },
                                                    'persons inside' : {
                                                 #                        'docents' : self.__persons['docent'],
                                                 #                        'participants' : self.__persons['participant']
                                                                       }
                                                 }
                             }
        for person_t, names in self.__persons.items():
            course_dict[f'{self.get_name()}']['persons inside'].update({person_t : names})

        return course_dict


    def add_person(self, name: str, db: DataBase, person_t: str):
        if len(self.__persons[person_t]) >= self.__max_counts[person_t]:
            raise OverflowError(f'the seminar "{self.__title}" is already full for {person_t}s')

        person = db.get(name)

        if not person:
            raise ValueError(f'there is no such a {person_t}: {name}, there are: {db.get_names()}')

        self.__persons[person_t].append(person.get_name())


    def delete_person(self, name: str, person_t: str, db: DataBase):
        person = db.get(name)
        person.free_up_time(self.__time_room)
        self.__persons[person_t].remove(name)


    def get_name(self) -> str:
        return self.__title


    def get_person_names(self, person_t: str) -> str:
        return ', '.join(self.__persons[person_t])


    def __str__(self) -> str:
        title = f'Titel: {self.__title}'
        docents = f'Dozierend: {self.get_person_names('docent')}'
        d = str(self.__date).split('-')
        date = f'Datum: {d[0]}-{d[1]}-{d[2]} um {d[3]}:{d[4]}:{d[5]} Uhr'
        duration = f'Dauer: {self.__duration} Minuten'
        place = f'Ort: {self.__place}'
        pl = f'Plätze: {len(self.__persons['participant'])} von {self.__max_counts['participant']} belegt'

        return f'{title}\n{docents}\n{date}\n{duration}\n{place}\n{pl}\n'