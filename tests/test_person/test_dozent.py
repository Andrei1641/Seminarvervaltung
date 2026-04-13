import unittest

from factories.persons_factory import PersonFactory


class DozentTest(unittest.TestCase):
    def test_dozent_ini_themen(self):
        with self.assertRaises(ValueError):
            PersonFactory.create_docent('vorname', 'nachname', 'mail@gmail.com', [])

        dozent = PersonFactory.create_docent('vorname', 'nachname', 'mail@gmail.com', ['bio', 'mat'])
        self.assertIn('Themen: bio, mat', str(dozent))


    def test_dozent_str(self):
        dozent = PersonFactory.create_docent('And', 'Sor', 'fsf@gmail.com', ['bio', 'mat'])

        result = str(dozent)

        self.assertIn('Name: And Sor\n', result)
        self.assertIn('Email-Adresse: fsf@gmail.com\n', result)
        self.assertIn('Rolle: Dozent\n', result)
        self.assertIn('Themen: bio, mat\n', result)