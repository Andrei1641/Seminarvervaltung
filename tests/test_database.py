import unittest
from types import NoneType

from classes.db import DataBase
from classes.person_classen import Participant, Docent
from factories.persons_factory import PersonFactory


class DataBaseTest(unittest.TestCase):
    def setUp(self):
        self.db_t = DataBase()
        self.db_d: DataBase = DataBase()

        self.t = PersonFactory.create_participant('Qnd', 'Lor', 'rkdd@gmail.com')
        self.t1 = PersonFactory.create_participant('Arr', 'Gmo', 'rkdd@gmail.com')

        self.d = PersonFactory.create_docent('Qnd', 'Lor', 'rkdd@gmail.com', ['bio', 'mat'])
        self.d1 = PersonFactory.create_docent('Qndd', 'Lor', 'rkdd@gmail.com', ['bio', 'mat'])

        self.db_t.insert_in_db(self.t)
        self.db_t.insert_in_db(self.t1)

        self.db_d.insert_in_db(self.d)
        self.db_d.insert_in_db(self.d1)

    def test_insert_in_db(self):
        #db can have only one type
        with self.assertRaises(ValueError):
            self.db_t.insert_in_db(self.d)

    def test_get_type(self):
        tmp: DataBase = DataBase()

        self.assertEqual(NoneType, tmp.get_type())

        self.assertEqual(Participant, self.db_t.get_type())
        self.assertEqual(Docent, self.db_d.get_type())


    def test_get_names(self):
        self.assertEqual('Lor Qnd, Gmo Arr', self.db_t.get_names())


    def test_get(self):
        self.assertEqual(self.t, self.db_t.get('Lor Qnd'))
        self.assertEqual(self.t1, self.db_t.get('Gmo Arr'))


    def test_pop(self):
        self.db_t.pop('Lor Qnd')
        self.assertEqual('Gmo Arr', self.db_t.get_names())


    def test_len(self):
        tmp: DataBase = DataBase()

        self.assertEqual(0, len(tmp))
        self.assertEqual(2, len(self.db_d))