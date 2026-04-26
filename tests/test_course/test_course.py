import unittest

from classes.course import Course
from classes.db import DataBase
from classes.person_classen import Participant, Docent
from factories.persons_factory import PersonFactory
from factories.course_factory import CourseFactory


class CourseTest(unittest.TestCase):
    def setUp(self):
        max_p: int = 9
        self.course1: Course = CourseFactory.create_course('Math', '2005-10-30-20-43-43', '30', str(max_p), 'klass 25')
        self.course2: Course = CourseFactory.create_course('Bio', '2005-10-30-20-0-0', '30', str(max_p), 'klass 25')

        self.db_p: DataBase = DataBase(Participant)
        self.db_d: DataBase = DataBase(Docent)

        self.db1: list[Participant] = []
        self.db2: list[Docent] = []

        for i in range(max_p + 1):
            self.db1.append(PersonFactory.create_participant(f'Qnd{chr(i + 97)}', 'Lor', 'rkdd@gmail.com'))
            self.db_p.insert_in_db(self.db1[i])

        for i in range(2+1):
            self.db2.append(PersonFactory.create_docent(f'Qnd{chr(i + 97)}', 'Lor', 'rkdd@gmail.com', ['bio', 'mat']))
            self.db_d.insert_in_db(self.db2[i])


    def test_add_participant(self):
        #it`s not a database with participant

        participant_from_db1 = self.db1[0].get_name()


        #unknown participant
        with self.assertRaises(ValueError):
            self.course1.add_person(participant_from_db1 + "vde", self.db_p, 'participant')

        #too many participant
        with self.assertRaises(OverflowError):
            for i in self.db1:
                self.course1.add_person(i.get_name(), self.db_p, 'participant')


    def test_add_docent(self):

        #unknown docent
        with self.assertRaises(ValueError):
            self.course1.add_person(self.db2[0].get_name() + "vde", self.db_d, "docent")

        #too many docents
        with self.assertRaises(OverflowError):
            for i in self.db2:
                self.course1.add_person(i.get_name(), self.db_d, "docent")

    def test_seminar_str(self):
        result = str(self.course1)

        self.assertIn('Titel: Math\n', result)
        self.assertIn('Datum: 2005-10-30 um 20:43:43 Uhr\n', result)
        self.assertIn('Dauer: 30 Minuten\n', result)
        self.assertIn('Ort: klass 25\n', result)
        self.assertIn('Plätze: 0 von 9 belegt\n', result)