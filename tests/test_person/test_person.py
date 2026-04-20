import unittest

from classes.data_time import DateTim
from factories.course_factory import CourseFactory
from factories.date_time_factory import DateTimeFactory
from factories.persons_factory import PersonFactory


class PersonTest(unittest.TestCase):
    #all func are adjusted for persons
    def test_name(self):
        test_cases = [('', 'Sor'),('And', ''),('', '')]

        #names have not to be empty
        for vorname, nachname in test_cases:
            with self.assertRaises(ValueError):
                PersonFactory.create_docent(vorname, nachname, 'mail@gmail.com', ['bio'])

        #names need to start with a capital letter
        person = PersonFactory.create_participant('vorname', 'nachname', 'mail@gmail.com')
        self.assertEqual('Nachname Vorname', person.get_name())

    def test_email_adresse(self):
        #email need: @
        with self.assertRaises(ValueError):
            PersonFactory.create_participant('vorname', 'nachname', 'mailgmail.com')

        #email with small letters
        person = PersonFactory.create_participant('vorname', 'nachname', 'MaiL@gmail.com')
        self.assertIn('Email-Adresse: mail@gmail.com', str(person))



    def setUp(self):
        self.person = PersonFactory.create_participant('N', 'N', 'd@')



    def test_get_dict(self):
        d_person1 = self.person.get_dict()

        d_await1: dict = {'N N' : {'first name' : 'N',
                                 'second name' : 'N',
                                 'email address' : 'd@',}
                        }

        self.assertEqual(d_await1, d_person1)

