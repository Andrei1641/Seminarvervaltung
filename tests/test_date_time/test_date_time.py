import unittest

from classes.data_time import DateTim
from factories.date_time_factory import DateTimeFactory


class DataTimIniTest(unittest.TestCase):

    def test_str(self):
        dt1: DateTim = DateTimeFactory.create_date_time('1999-10-10-10-10-10')
        self.assertEqual('1999-10-10-10-10-10', str(dt1))

    def test_compare_equal(self):
        test_times1 = ['2000-5-5-5-5-5', '2000-6-5-5-3-20']
        test_times2 = ['2000-5-5-5-5-5', '2000-6-5-5-3-20']

        for i in range(len(test_times1)):
            dt1: DateTim = DateTimeFactory.create_date_time(test_times1[i])
            dt2: DateTim = DateTimeFactory.create_date_time(test_times2[i])
            self.assertEqual(True, dt1 == dt2)


    def test_compare_lt(self):
        test_times1 = ['1999-10-10-10-10-10', '2000-5-5-5-3-20', '2000-5-5-5-3-15']
        test_times2 = ['2000-5-5-5-5-5', '2000-6-5-5-3-20', '2000-5-5-5-3-20']

        for i in range(len(test_times1)):
            dt1: DateTim = DateTimeFactory.create_date_time(test_times1[i])
            dt2: DateTim = DateTimeFactory.create_date_time(test_times2[i])
            self.assertEqual(True, dt1 < dt2)


    def test_compare_type_error(self):
        dt1: DateTim = DateTimeFactory.create_date_time('1999-10-10-10-10-10')
        test_date = [0, '', 'f', 0.1]
        for i in test_date:
            with self.assertRaises(TypeError):
                dt1 < i


    def test_add(self):
        test_date = [(0,0,0,0,0,0),   (0,0,0,0,0,20),    (0,0,0,0,0,60),   (0,0,0,0,20,0),    (0,0,0,0,60,0),
                     (0,0,0,5,0,0),     (0,0,0,24,0,0),  (0,0,5,0,0,0),     (0,0,40,0,0,0),    (0,1,0,0,0,0),
                     (0,12,0,0,0,0),  (5,0,0,0,0,0),    (0,0,0,10,0,60),   (0,0,0,0,5,60)]
        result = [  '2000-5-5-5-5-5', '2000-5-5-5-5-25', '2000-5-5-5-6-5', '2000-5-5-5-25-5', '2000-5-5-6-5-5',
                    '2000-5-5-10-5-5', '2000-5-6-5-5-5', '2000-5-10-5-5-5', '2000-6-14-5-5-5', '2000-6-5-5-5-5',
                    '2001-5-5-5-5-5', '2005-5-5-5-5-5', '2000-5-5-15-6-5', '2000-5-5-5-11-5']

        for i in range(len(test_date)):
            date_time = DateTimeFactory.create_date_time('2000-5-5-5-5-5')
            date_time.add_time(years=test_date[i][0], months=test_date[i][1], days=test_date[i][2],
                               hours=test_date[i][3], minutes=test_date[i][4], seconds=test_date[i][5])

            self.assertEqual(result[i], str(date_time))