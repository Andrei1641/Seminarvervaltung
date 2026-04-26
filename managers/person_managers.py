from abc import abstractmethod

from classes.course import Course
from classes.db import DataBase
from classes.person_classen import Docent, Participant
from factories.persons_factory import PersonFactory
from interfaces.manager import Manager


class PersonManager(Manager):

    person_managers: dict = {}

    def find_func(self, *args):
        action = args[0]
        if action == 'create':
            self.create(*args[1:])
        elif action == 'add':
            self.add(*args[1:])
        elif action == 'show':
            self.show()
        elif action == 'delete':
            if args[1] == 'from_db':
                self.delete_from_db(*args[2:])
            if args[1] == 'from_course':
                self.delete_from_course(*args[2:])
        elif action == 'info':
            self.info(*args[1:])


    @staticmethod
    def person_daten() -> tuple[str, str, str]:
        first_name: str = input('Vorname: ')
        second_name: str = input('Nachname: ')
        email_address: str = input('email_address: ')
        return first_name, second_name, email_address

    @staticmethod
    def _ad(name: str, title: str, db: DataBase, course_db: DataBase, person_t: str):
        course: Course = course_db.get(title)
        if not course:
            raise ValueError(f'there is no such a course: {title}, there are: {course_db.get_names()}')

        # book time person
        course.add_person(name, db, person_t)

        person = db.get(name)

        if not person:
            raise ValueError(
                f'there is no such a {person_t}: {name}, there are: {db.get_names()}')

        course_start, course_end = course.get_time_room()

        person.book_time(course_start, course_end, title)


    @staticmethod
    def _del_from_db(name: str, db: DataBase, course_db: DataBase, person_t: str):
        db.pop(name)
        course_names = course_db.get_names()

        if course_names:
            course_names = course_names.split(', ')
            # can be optimized (each person has name of course,that he visit)
            for name in course_names:
                s_db: Course = course_db.get(name)
                s_db.delete_person(name, person_t, db)


    @abstractmethod
    def get_db(self) -> DataBase:
        ...

    @abstractmethod
    def create(self, first_name = '', second_name = '', email_address = ''):
        ...

    @abstractmethod
    def add(self, name: str, title: str):
        ...

    @abstractmethod
    def show(self):
        ...

    @abstractmethod
    def delete_from_course(self, name: str, title: str):
        ...

    @abstractmethod
    def delete_from_db(self, name: str):
        ...

    @abstractmethod
    def info(self, name: str):
        ...


class ParticipantManager(PersonManager):
    def __init__(self, course: DataBase):
        self.__type: type = Participant
        self.__db: DataBase = DataBase(Participant)
        self.__course_db: DataBase = course
        ParticipantManager.person_managers.update({'participant':self})


    def get_db(self) -> DataBase:
        return self.__db

    def get_type(self) -> type:
        return self.__type


    def get_dict(self) -> dict:
        d = ParticipantManager._get_d(self.__db, 'participants')
        return d


    def create(self, first_name = '', second_name = '', email_address = ''):
        if not (first_name and second_name and email_address):
            first_name, second_name, email_address = ParticipantManager.person_daten()

        new_participant = PersonFactory.create_participant(first_name, second_name, email_address)
        self.__db.insert_in_db(new_participant)


    def add(self, name: str, title: str):
        ParticipantManager._ad(name, title, self.__db, self.__course_db, 'participant')


    def delete_from_course(self, name: str, title: str):
        course: Course = self.__course_db.get(title)
        course.delete_person(name, 'participant', self.__db)


    def show(self):
        print(self.__db.get_names())


    def delete_from_db(self, name: str):
        ParticipantManager._del_from_db(name, self.__db, self.__course_db, 'participant')


    def info(self, name: str):
        print(self.__db.get(name))


class DocentManager(PersonManager):
    def __init__(self, course: DataBase):
        self.__type = Docent
        self.__type_str = 'docent'
        self.__db: DataBase = DataBase(Docent)
        self.__course_db: DataBase = course
        DocentManager.person_managers.update({'docent':self})

    def get_type_str(self):
        return self.__type_str

    def get_db(self) -> DataBase:
        return self.__db


    def get_type(self) -> type:
        return self.__type


    def get_dict(self) -> dict:
        d = DocentManager._get_d(self.__db, 'docents')
        return d


    def create(self, first_name = '', second_name = '', email_address = '', list_an_themes = ''):
        if not (first_name and second_name and email_address and list_an_themes):
            first_name, second_name, email_address = DocentManager.person_daten()
            list_an_themes = (input('list an themes(at least one) eingeben: ')).strip()
            if list_an_themes:
                list_an_themes = list_an_themes.split(', ')

        new_docent = PersonFactory.create_docent(first_name, second_name, email_address, list_an_themes)
        self.__db.insert_in_db(new_docent)


    def add(self, name: str, title: str):
        DocentManager._ad(name, title, self.__db, self.__course_db, 'docent')


    def delete_from_course(self, name: str, title: str):
        course: Course = self.__course_db.get(title)
        course.delete_person(name, 'docent', self.__db)


    def delete_from_db(self, name: str):
        DocentManager._del_from_db(name, self.__db, self.__course_db, 'docent')


    def show(self):
        print(self.__db.get_names())


    def info(self, name: str):
        print(self.__db.get(name))
