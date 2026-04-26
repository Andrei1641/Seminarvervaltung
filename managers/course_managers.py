from classes.course import Course
from classes.db import DataBase
from factories.course_factory import CourseFactory
from interfaces.manager import Manager


class CourseManager(Manager):
    def __init__(self):
        self.__type = Course
        self.__db: DataBase = DataBase(Course)


    def find_func(self, *args):
        action = args[0]
        per = 'p'
        if len(args) > 1:
            per = args[1]

        if action == 'create':
            self.create(*args[1:])
        elif action == 'show' and per == 'person':
            self.show_inside(*args[2:])
        elif action == 'show':
            self.show()
        elif action == 'delete':
            self.delete(*args[1:])
        elif action == 'info':
            self.info(*args[1:])


    def create(self, title = '', date = '', duration = '', max_participant_count = '', place = ''):
        if not (title and date and duration and max_participant_count and place):
            title: str = input('Titel: ')
            date: str = input('Datum(YYYY-MM-DD-HH-MM-SS): ')
            duration = input('Dauer: ')
            max_participant_count: str = input('Maximale Teilnehmerzahl: ')
            place: str = input('Ort: ')

        new_course = CourseFactory.create_course(title, date, str(duration), str(max_participant_count), place)
        self.__db.insert_in_db(new_course)


    def get_type(self) -> type:
        return self.__type


    def get_db(self):
        return self.__db


    def get_dict(self) -> dict:
        d = CourseManager._get_d(self.__db, 'courses')
        return d


    def show(self):
        print(self.__db.get_names())


    def show_inside(self, title: str):
        course: Course = self.__db.get(title)

        person_t = course.get_persons_t()

        for t in person_t:
            print(f'{t} = {course.get_person_names(t)}')


    def delete(self, title: str):
        course: Course = self.__db.get(title)
        managers = PersonManager.person_managers
        person_t = course.get_persons_t()

        for t in person_t:
            manager = managers.get(t)

            names: str = course.get_person_names(t)
            d = names.split(', ')
            if d != ['']:
                for i in d:
                    course.delete_person(i, t, manager.get_db())

        self.__db.pop(title)


    def info(self, title: str):
        print(self.__db.get(title))