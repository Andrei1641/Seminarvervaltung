import copy
from classes.data_time import DateTim

from classes.db import DataBase
from classes.person_classen import Docent, Participant
from interfaces.nameable import Nameable
from interfaces.serializable import Serializable


class Course(Nameable, Serializable):
    def __init__(self, title: str, date: DateTim, duration: int, max_participant_count: int, place: str):
        self.__title: str = title
        self.__date: DateTim = date
        self.__duration: int = duration      #min
        self.__max_participant_count: int = max_participant_count
        self.__place: str = place
        self.__docents: DataBase = DataBase()
        self.__participants: DataBase = DataBase()
        self.__time_room = self.adjust_time_room()


    def get_time_room(self):
        return self.__time_room

    def adjust_time_room(self) -> tuple[DateTim, DateTim]:

        course_start = self.__date

        course_end = copy.copy(self.__date)
        course_end.add_time(minutes=self.__duration)

        return course_start, course_end

    def get_dict(self) -> dict:


        course_dict: dict = {
                                self.get_name(): {
                                                    'course info' : {
                                                                        'title' : self.__title,
                                                                        'date' : str(self.__date),
                                                                        'duration' : self.__duration,
                                                                        'max participant count' : self.__max_participant_count,
                                                                        'place' : self.__place
                                                                    },
                                                    'persons inside' : {
                                                                        'docents' : self.__docents.get_names(),
                                                                        'participants' : self.__participants.get_names()
                                                                       }
                                                 }
                             }

        return course_dict

    def add_docent(self, docent_name: str, docent_db: DataBase):

        if docent_db.get_type() != Docent:
            raise ValueError(f'it`s not a database with docents')
        elif len(self.__docents) >= 2:
            raise OverflowError(f'the seminar "{self.__title}" is already full for docents')

        docent = docent_db.get(docent_name)



        if not docent:
            raise ValueError(f'there is no such a docent: {docent_name}, there are: {docent_db.get_names()}')

        self.__docents.insert_in_db(docent)


    def add_participant(self, participant_name: str, participant_db: DataBase):

        if participant_db.get_type() != Participant:
            raise ValueError(f'it`s not a database with participant')
        elif len(self.__participants) >= self.__max_participant_count:
            raise OverflowError(f'the seminar "{self.__title}" is already full for participant')

        participant = participant_db.get(participant_name)

        if not participant:
            raise ValueError(f'there is no such a participant: {participant_name}, there are: {participant_db.get_names()}')

        self.__participants.insert_in_db(participant)


    def delete_docent(self, docent_name: str):
        docent: Docent = self.__docents.get(docent_name)
        docent.free_up_time(self.__time_room)
        self.__docents.pop(docent_name)


    def delete_participant(self, participant_name: str):
        participant: Participant = self.__participants.get(participant_name)
        participant.free_up_time(self.__time_room)
        self.__participants.pop(participant_name)

    def get_name(self) -> str:
        return self.__title

    def get_docents_names(self):
        return self.__docents.get_names()

    def get_participant_names(self):
        return self.__participants.get_names()

    def __str__(self) -> str:
        title = f'Titel: {self.__title}'
        docents = f'Dozierend: {self.__docents.get_names()}'
        d = str(self.__date).split('-')
        date = f'Datum: {d[0]}-{d[1]}-{d[2]} um {d[3]}:{d[4]}:{d[5]} Uhr'
        duration = f'Dauer: {self.__duration} Minuten'
        place = f'Ort: {self.__place}'
        pl = f'Plätze: {len(self.__participants)} von {self.__max_participant_count} belegt'

        return f'{title}\n{docents}\n{date}\n{duration}\n{place}\n{pl}\n'