import json
import os.path
from json import JSONDecodeError
import copy

from classes.data_time import DateTim
from classes.person_classen import Docent, Participant
from classes.course import Course
from factories.persons_factory import PersonFactory
from factories.course_factory import CourseFactory
from classes.db import DataBase
from interfaces.serializable import Serializable


class Information(Serializable):
    def __init__(self):
        self.__docent_db = DataBase()
        self.__participant_db = DataBase()
        self.__course_db = DataBase()


    def deserialize(self):
        data: dict = {}
        if os.path.exists('data.json'):
            try:
                with open('data.json', "r") as f:
                    data = json.load(f)
            except JSONDecodeError:
                return
        else:
            return

        if data['all docents'] != '':
            for i in data['all docents'].values():
                docent = PersonFactory.create_docent(i['first name'], i['second name'], i['email address'], i['theme'])
                # if i['booked time']:
                #     docent.deserialize_booked_time(i['booked time'])

                self.__docent_db.insert_in_db(docent)


        if data['all participants'] != '':
            for i in data['all participants'].values():
                participant = PersonFactory.create_participant(i['first name'], i['second name'], i['email address'])
                self.__participant_db.insert_in_db(participant)

        if data['all courses'] != '':
            for i in data['all courses'].values():
                course_info = i['course info']
                course: Course = CourseFactory.create_course(course_info['title'], course_info['date'], course_info['duration'],
                                                             course_info['max participant count'], course_info['place'])

                self.__course_db.insert_in_db(course)

                persons_inside = i['persons inside']

                # add docents
                docents_inside: str = persons_inside['docents']
                docent_name_inside: list[str] = docents_inside.split(', ')

                if docent_name_inside != ['']:
                    for j in docent_name_inside:
                        self.add_docent_to_course(j, course.get_name())

                #add participants
                participants_inside: str = persons_inside['participants']
                participant_name_inside: list[str] = participants_inside.split(', ')

                if participant_name_inside != ['']:
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
        all_courses: list[Serializable] = Information.__db_get_objects(self.__course_db)

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

        list_an_themes = list_an_themes.split(', ')

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

        new_course = CourseFactory.create_course(title, date, duration, max_participant_count, place)
        self.__course_db.insert_in_db(new_course)


    def add_docent_to_course(self, docent_name: str, course_title: str):
        course: Course = self.__course_db.get(course_title)
        if not course:
            raise ValueError(f'there is no such a course: {course_title}, there are: {self.__course_db.get_names()}')

        #book time docent
        course.add_docent(docent_name, self.__docent_db)

        docent: Docent = self.__docent_db.get(docent_name)

        if not docent:
            raise ValueError(f'there is no such a docent: {docent_name}, there are: {self.__docent_db.get_names()}')

        course_start, course_end = course.get_time_room()

        docent.book_time(course_start, course_end, course_title)


    def add_participant_to_course(self, participant_name: str, course_title: str):
        course: Course = self.__course_db.get(course_title)
        if not course:
            raise ValueError(f'there is no such a course: {course_title}, there are: {self.__course_db.get_names()}')

        # book time participant
        course.add_participant(participant_name, self.__participant_db)

        participant: Participant = self.__participant_db.get(participant_name)

        if not participant:
            raise ValueError(f'there is no such a docent: {participant_name}, there are: {self.__participant_db.get_names()}')

        course_start, course_end = course.get_time_room()

        participant.book_time(course_start, course_end, course_title)


    def show_course(self, persons_type: str, course_name: str):
        if persons_type == 'participant':
            course: Course = self.__course_db.get(course_name)
            print(course.get_participant_names())
        if persons_type == 'docent':
            course: Course = self.__course_db.get(course_name)
            print(course.get_docents_names())


    def show_all(self, db_type: str):
        if db_type == 'participant':
            print(self.__participant_db.get_names())
        if db_type == 'docent':
            print(self.__docent_db.get_names())
        if db_type == 'course':
            print(self.__course_db.get_names())


    def delete_from_course(self, person_type: str, person_name: str, course_name: str):
        if person_type == 'participant':
            course: Course = self.__course_db.get(course_name)
            course.delete_participant(person_name)
        if person_type == 'docent':
            course: Course = self.__course_db.get(course_name)
            course.delete_docent(person_name)


    def delete_from_db(self, person_type: str, person_name: str):
        if person_type == 'participant':
            self.__participant_db.pop(person_name)
            seminar_names = self.__course_db.get_names()

            if seminar_names:
                seminar_names = seminar_names.split(', ')
                #can be optimized (each person has name of course,that he visit)
                for name in seminar_names:
                    s_db: Course = self.__course_db.get(name)
                    s_db.delete_participant(person_name)

        if person_type == 'docent':
            self.__docent_db.pop(person_name)
            seminar_names = self.__course_db.get_names()
            if seminar_names:
                seminar_names = seminar_names.split(', ')
                # can be optimized (each person has name of course,that he visit)
                for name in seminar_names:
                    s_db: Course = self.__course_db.get(name)
                    s_db.delete_docent(person_name)


    def delete_course(self, course_title: str):
        course: Course = self.__course_db.get(course_title)

        docents_names: str = course.get_docents_names()
        d = docents_names.split(', ')
        for i in d:
            self.delete_from_course('docent', i, course_title)

        participants_names: str = course.get_participant_names()
        p = participants_names.split(', ')
        for i in p:
            self.delete_from_course('participant', i, course_title)

        self.__course_db.pop(course_title)


    def info_docent(self, docent_name: str):
        print(self.__docent_db.get(docent_name))


    def info_participant(self, participant_name: str):
        print(self.__participant_db.get(participant_name))


    def info_course(self, course_name: str):
        print(self.__course_db.get(course_name))