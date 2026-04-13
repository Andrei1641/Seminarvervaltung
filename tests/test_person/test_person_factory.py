import unittest

from factories.persons_factory import PersonFactory


class PersonIni(unittest.TestCase):
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