from classes.seminar import Seminar
from factories.persons_factory import PersonFactory
from factories.seminar_factory import SeminarFactory
from classes.db import DataBase

class Information:
    def __init__(self):
        self.__docent_db = DataBase()
        self.__participant_db = DataBase()
        self.__seminar_db = DataBase()

    @staticmethod
    def __person_daten():
        first_name: str = input('Vorname: ')
        second_name: str = input('Nachname: ')
        email_address: str = input('email_address: ')
        return first_name, second_name, email_address

    def docent_create(self):
        first_name, second_name, email_address = Information.__person_daten()
        list_an_themes = input('list an themes(at least one) eingeben: ')

        list_an_themes.replace(' ', '')
        list_an_themes = list_an_themes.split(',')

        new_dozent = PersonFactory.create_docent(first_name, second_name, email_address, list_an_themes)
        self.__docent_db.insert_in_db(new_dozent)


    def participant_create(self):
        first_name, second_name, email_address = Information.__person_daten()

        new_participant = PersonFactory.create_participant(first_name, second_name, email_address)
        self.__participant_db.insert_in_db(new_participant)


    def course_create(self):
        title: str = input('Titel: ')
        date: str = input('Datum(YYYY-MM-DD-HH-MM-SS): ')
        duration: int = int(input('Dauer: '))
        max_participant_count: int = int(input('Maximale Teilnehmerzahl: '))
        place: str = input('write ort: ')

        new_course = SeminarFactory.create_seminar(title, date, duration, max_participant_count, place)
        self.__seminar_db.insert_in_db(new_course)



    def add_docent_to_course(self, docent_name: str, course_title: str):
        course: Seminar = self.__seminar_db.get(course_title)
        if not course:
            raise ValueError(f'there is no such a course: {course_title}, there are: {self.__seminar_db.get_names()}')


        course.add_docent(docent_name, self.__docent_db)


    def add_participant_to_course(self, participant_name: str, course_title: str):
        course: Seminar = self.__seminar_db.get(course_title)
        if not course:
            raise ValueError(f'there is no such a course: {course_title}, there are: {self.__seminar_db.get_names()}')

        course.add_participant(participant_name, self.__participant_db)


    def show_course(self, persons_type: str, course_name: str):
        if persons_type == 'participant':
            course: Seminar = self.__seminar_db.get(course_name)
            print(course.get_participant_names())
        if persons_type == 'docent':
            course: Seminar = self.__seminar_db.get(course_name)
            print(course.get_docents_names())


    def show_all(self, db_type: str):
        if db_type == 'participant':
            print(self.__participant_db.get_names())
        if db_type == 'docent':
            print(self.__docent_db.get_names())
        if db_type == 'course':
            print(self.__seminar_db.get_names())


    def delete_from_course(self, person_type: str, person_name: str, course_name: str):
        if person_type == 'participant':
            course: Seminar = self.__seminar_db.get(course_name)
            course.delete_participant(person_name)
        if person_type == 'docent':
            course: Seminar = self.__seminar_db.get(course_name)
            course.delete_docent(person_name)

    def delete_from_db(self, person_type: str, person_name: str):
        if person_type == 'participant':
            self.__participant_db.pop(person_name)
            seminar_names = self.__seminar_db.get_names()
            seminar_names = seminar_names.split(', ')

            for name in seminar_names:
                s_db: Seminar = self.__seminar_db.get(name)
                s_db.delete_participant(person_name)

        if person_type == 'docent':
            self.__docent_db.pop(person_name)
            seminar_names = self.__seminar_db.get_names()
            seminar_names = seminar_names.split(', ')

            for name in seminar_names:
                s_db: Seminar = self.__seminar_db.get(name)
                s_db.delete_docent(person_name)


    def delete_course(self, course_title: str):
        self.__seminar_db.pop(course_title)


    def info_docent(self, docent_name: str):
        print(self.__docent_db.get(docent_name))


    def info_participant(self, participant_name: str):
        print(self.__participant_db.get(participant_name))


    def info_course(self, course_name: str):
        print(self.__seminar_db.get(course_name))