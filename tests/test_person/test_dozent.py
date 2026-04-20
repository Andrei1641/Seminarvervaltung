import unittest

from factories.persons_factory import PersonFactory


class DozentTest(unittest.TestCase):
    def setUp(self):
        self.docent = PersonFactory.create_docent('vorname', 'nachname', 'mail@gmail.com', ['bio', 'mat'])


    def test_dozent_ini_themen(self):
        with self.assertRaises(ValueError):
            PersonFactory.create_docent('vorname', 'nachname', 'mail@gmail.com', [])

        self.assertIn('Themen: bio, mat', str(self.docent))


    def test_dozent_str(self):
        result = str(self.docent)

        self.assertIn('Name: Vorname Nachname\n', result)
        self.assertIn('Email-Adresse: mail@gmail.com\n', result)
        self.assertIn('Rolle: Dozent\n', result)
        self.assertIn('Themen: bio, mat\n', result)


    def test_get_dict(self):
        d: dict = self.docent.get_dict()
        self.assertEqual(["bio", "mat"], d['Nachname Vorname']['theme'])