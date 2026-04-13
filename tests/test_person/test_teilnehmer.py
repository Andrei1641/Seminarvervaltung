import unittest

from factories.persons_factory import PersonFactory


class TeilnehmerTest(unittest.TestCase):
    def test_teilnehmer_str(self):
        teilnehmer = PersonFactory.create_participant('Qnd', 'Lor', 'rkdd@gmail.com')

        result = str(teilnehmer)

        self.assertIn('Name: Qnd Lor\n', result)
        self.assertIn('Email-Adresse: rkdd@gmail.com\n', result)
        self.assertIn('Rolle: Teilnehmer\n', result)