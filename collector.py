import json
import os.path
from json import JSONDecodeError

from classes.person_classen import Docent, Participant
from classes.seminar import Seminar
from factories.persons_factory import PersonFactory
from factories.seminar_factory import SeminarFactory
from classes.db import DataBase
from interfaces.serializable import Serializable


class Information(Serializable):
    def __init__(self):
        self.__docent_db = DataBase()
        self.__participant_db = DataBase()
        self.__seminar_db = DataBase()


    def deserialize(self):
        data: dict = {}
        if os.path.exists('data.json'):
            try:
                with open('data.json', "r") as f:
                    data = json.load(f)
            except JSONDecodeError:
                return

        for i in data['all docents'].values():
            docent = PersonFactory.create_docent(i['first name'], i['second name'], i['email address'], i['theme'])
            self.__docent_db.insert_in_db(docent)


        for i in data['all participants'].values():
            participant = PersonFactory.create_participant(i['first name'], i['second name'], i['email address'])
            self.__participant_db.insert_in_db(participant)


        for i in data['all courses'].values():
            course_info = i['course info']
            course: Seminar = SeminarFactory.create_seminar(course_info['title'], course_info['date'], course_info['duration'],
                                                   course_info['max participant count'], course_info['place'])

            self.__seminar_db.insert_in_db(course)

            persons_inside = i['persons inside']

            # add docents
            docents_inside: str = persons_inside['docents']
            docent_name_inside: list[str] = docents_inside.split(', ')

            for j in docent_name_inside:
                self.add_docent_to_course(j, course.get_name())

            #add participants
            participants_inside: str = persons_inside['participants']
            participant_name_inside: list[str] = participants_inside.split(', ')

            for j in participant_name_inside:
                self.add_participant_to_course(j, course.get_name())




    @staticmethod
    def __db_get_objects(db: DataBase) -> list[Serializable]:
        all_names = db.get_names()
        all_names = all_names.split(', ')
        all_ob: list[Serializable] = []

        for i in all_names:
            all_ob.append(db.get(i))

        return all_ob

    def get_dict(self) -> dict:
        #docent dict
        all_docents: list[Serializable] = Information.__db_get_objects(self.__docent_db)

        docents_dict: dict = {'all docents' : {}}

        if all_docents != [0]:
            for i in all_docents:
                docents_dict['all docents'].update(i.get_dict())
        else:
            docents_dict['all docents'] = ''


        #participant dict
        all_participants: list[Serializable] = Information.__db_get_objects(self.__participant_db)

        participants_dict: dict = {'all participants' : {}}

        if all_participants != [0]:
            for i in all_participants:
                participants_dict['all participants'].update(i.get_dict())
        else:
            participants_dict['all participants'] = ''


        #course dict
        all_courses: list[Serializable] = Information.__db_get_objects(self.__seminar_db)

        courses_dict: dict = {'all courses' : {}}

        if all_courses != [0]:
            for i in all_courses:
                courses_dict['all courses'].update(i.get_dict())
        else:
            courses_dict['all courses'] = ''

        #serialize
        serialize_dict: dict = docents_dict | participants_dict | courses_dict

        return serialize_dict


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