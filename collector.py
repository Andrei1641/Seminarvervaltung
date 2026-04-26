import json
import os.path
from json import JSONDecodeError

from classes.course import Course
from classes.person_classen import Participant, Docent, Person
from interfaces.manager import Manager


class Information:
    def __init__(self, managers: list[Manager]):
        self.__managers = managers
        self.__class_map: dict[str, type] = {'participant' : Participant, 'course': Course, 'docent': Docent}


    def serialize(self):
        d: dict = self.get_dict()
        if d:
            with open('data.json', "w") as f:
                json.dump(d, f, indent=4)


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

        #persons
        person_roles: dict = data['persons']

        for i in person_roles.keys():
            role = i
            role = role[4:len(role)-1]
            for persons in person_roles[i]:
                f = []
                for feature in person_roles[i][persons].values():
                    f.append(feature)

                self.find_manager(role, 'create', *f)

        #courses
        course_types: dict = data['courses']

        for i in course_types.keys():
            courses = i
            courses = courses[4:len(courses)-1]
            if course_types['all courses'] != '':
                for course in course_types[i].values():
                    course_info: dict = course['course info']

                    info = []
                    for inf in course_info.values():
                        info.append(inf)
                    self.find_manager(courses, 'create', *info)

                    persons_inside: dict = course['persons inside']

                    person_role_names = []
                    for per in persons_inside.items():
                        person_role_names.append(per)

                    for role, names in person_role_names:
                        if names != ['']:
                            for n in names:
                                self.find_manager(role, 'add', n, course['course info']['title'])




    def get_dict(self) -> dict:
        d = {
            "persons": {},
            "courses": {}
        }

        for manager in self.__managers:
            if issubclass(manager.get_type(), Person):
                d["persons"].update(manager.get_dict())
            else:
                d["courses"].update(manager.get_dict())

        return d


    def find_manager(self, t: str, *args):
        typ: type = self.__class_map[t]

        #can be optimized
        for i in self.__managers:
            if typ == i.get_type():
                i.find_func(*args)