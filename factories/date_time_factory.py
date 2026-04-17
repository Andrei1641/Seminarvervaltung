from classes.data_time import DateTim


class DateTimeFactory:
    @staticmethod
    def create_date_time(date_time: str):
        s = date_time.split('-')

        if len(s) != 6:
            raise ValueError('date has inappropriate format (YYYY-MM-DD-HH-MM-SS)')

        for i in s:
            if not i.isdigit():
                raise ValueError('date can not consist letter')
            if int(i) < 0:
                raise ValueError('date can not be negative')

        #year
        if len(s[0]) != 4:
            raise ValueError('it is out of observing years')

        s = [int(i) for i in s]

        year = s[0]
        mon = s[1]
        day = s[2]
        hour = s[3]
        minute = s[4]
        second = s[5]

        months: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if mon > 12:
            raise ValueError('the months can not be higher then 12')

        if day > months[mon - 1]:
            raise ValueError(f'the days can not be higher then {months[mon - 1]} in {mon} month')

        if hour > 23:
            raise ValueError('the hours can not be higher then 23')
        if minute > 59:
            raise ValueError('the minutes can not be higher then 59')
        if second > 59:
            raise ValueError('the seconds can not be higher then 59')

        return DateTim(year, mon, day, hour, minute, second)