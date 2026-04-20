import unittest

from factories.course_factory import CourseFactory


class SeminarIniTest(unittest.TestCase):
    def test_str_init(self):
        #titel can not be empty
        titel = ['', '   ']

        for i in titel:
            with self.assertRaises(ValueError):
                CourseFactory.create_course(i, '2005-10-30-20-43-43', 30, 10, 'klass 25')


    def test_ints_init(self):
        with self.assertRaises(ValueError):
            CourseFactory.create_course('Titel Name', '2005-10-30-20-43-43', -1, 10, 'klass 25')
