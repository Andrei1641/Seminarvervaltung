import unittest

from classes.course import Course
from classes.db import DataBase
from classes.person_classen import Participant, Docent
from factories.persons_factory import PersonFactory
from factories.course_factory import CourseFactory


class CourseTest(unittest.TestCase):
    def setUp(self):
        max_p: int = 9
        self.course1: Course = CourseFactory.create_course('Math', '2005-10-30-20-43-43', 30, max_p, 'klass 25')
        self.course2: Course = CourseFactory.create_course('Bio', '2005-10-30-20-0-0', 30, max_p, 'klass 25')

        self.db_p: DataBase = DataBase()
        self.db_d: DataBase = DataBase()

        self.db1: list[Participant] = []
        self.db2: list[Docent] = []

        for i in range(max_p + 1):
            self.db1.append(PersonFactory.create_participant(f'Qnd{chr(i)}', 'Lor', 'rkdd@gmail.com'))
            self.db_p.insert_in_db(self.db1[i])

        for i in range(2+1):
            self.db2.append(PersonFactory.create_docent(f'Qnd{chr(i)}', 'Lor', 'rkdd@gmail.com', ['bio', 'mat']))
            self.db_d.insert_in_db(self.db2[i])


    def test_add_participant(self):
        #it`s not a database with participant
        with self.assertRaises(ValueError):
            participant_from_db1 = self.db1[0].get_name()
            self.course1.add_participant(participant_from_db1, self.db_d)

        #unknown participant
        with self.assertRaises(ValueError):
            self.course1.add_participant(participant_from_db1 + "vde", self.db_p)

        #too many participant
        with self.assertRaises(OverflowError):
            for i in self.db1:
                self.course1.add_participant(i.get_name(), self.db_p)


    def test_add_docent(self):
        #it`s not a database with docents
        with self.assertRaises(ValueError):
            self.course1.add_docent(self.db2[0].get_name(), self.db_p)

        #unknown docent
        with self.assertRaises(ValueError):
            self.course1.add_docent(self.db2[0].get_name() + "vde", self.db_d)

        #too many docents
        with self.assertRaises(OverflowError):
            for i in self.db2:
                self.course1.add_docent(i.get_name(), self.db_d)

    def test_seminar_str(self):
        result = str(self.course1)

        self.assertIn('Titel: Math\n', result)
        self.assertIn('Datum: 2005-10-30 um 20:43:43 Uhr\n', result)
        self.assertIn('Dauer: 30 Minuten\n', result)
        self.assertIn('Ort: klass 25\n', result)
        self.assertIn('Plätze: 0 von 9 belegt\n', result)