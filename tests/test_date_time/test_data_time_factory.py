import unittest

from factories.date_time_factory import DateTimeFactory


class DataTimIniTest(unittest.TestCase):
    def test_data_time_ini_inappropriate_format(self):
        test_date = ["2000-5-5-5-5", "2000-5-5-5-5-5-5", "2000- - - - - -", ""]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)


    def test_data_time_ini_not_digit(self):
        test_date = ["2000-5-5-5-5-a", "2000-b-5-5-5-a"]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)


    def test_data_time_ini_out_of_observing_years(self):
        test_date = ["200-5-5-5-5-5", "20000-5-5-5-5-5"]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)


    def test_data_time_ini_months(self):
        test_date = ["2000-13-5-5-5-5", "2000-20-5-5-5-5"]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)


    def test_data_time_ini_hours(self):
        test_date = ["2000-10-5-60-5-5", "2000-10-5-70-5-5"]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)


    def test_data_time_ini_minutes(self):
        test_date = ["2000-10-5-5-70-5", "2000-10-5-5-100-5"]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)


    def test_data_time_ini_seconds(self):
        test_date = ["2000-10-5-5-5-60", "2000-10-5-5-5-70"]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)

    def test_data_time_ini_days(self):
        test_date = ["2000-4-31-5-5-5", "2000-2-30-5-5-5", "2000-5-50-5-5-5"]

        for i in test_date:
            with self.assertRaises(ValueError):
                DateTimeFactory.create_date_time(i)