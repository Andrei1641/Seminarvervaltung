import unittest

from factories.persons_factory import PersonFactory


class ParticipantTest(unittest.TestCase):
    def test_participant_str(self):
        participant = PersonFactory.create_participant('Qnd', 'Lor', 'rkdd@gmail.com')

        result = str(participant)

        self.assertIn('Name: Qnd Lor\n', result)
        self.assertIn('Email-Adresse: rkdd@gmail.com\n', result)
        self.assertIn('Rolle: Teilnehmer\n', result)