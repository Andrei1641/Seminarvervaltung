from classes.seminar import Seminar

class SeminarFactory:

    @staticmethod
    def __date_check(date: str) -> str:
        s = date.split('-')

        if len(s) != 6:
            raise ValueError('date has inappropriate format (YYYY-MM-DD-HH-MM-SS)')

        for i in s:
            if not i.isdigit():
                raise ValueError('date can not consist letter')
            if int(i) < 0:
                raise ValueError('date can not be negative')

        if len(s[0]) != 4:
            raise ValueError('it is out of observing years')

        mon = int(s[1])
        day = int(s[2])
        months: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if mon > 12:
            raise ValueError('the months can not be higher then 12')

        if day > months[mon-1]:
            raise ValueError(f'the days can not be higher then {months[mon-1]} in {mon} month')

        if int(s[3]) > 23:
            raise ValueError('the hours can not be higher then 23')
        if int(s[4]) > 59:
            raise ValueError('the minutes can not be higher then 59')
        if int(s[5]) > 59:
            raise ValueError('the seconds can not be higher then 59')

        return date


    @staticmethod
    def create_seminar(title: str, date: str, duration: int, max_participant_count: int, place: str) -> Seminar:

        if not title.strip():
            raise ValueError('title can not be empty')
        if not place:
            raise ValueError('place can not be empty')
        if duration <= 0:
            raise ValueError('duration need to be higher than 0')
        if max_participant_count <= 0:
            raise ValueError('max participant count need to be higher than 0')

        date = SeminarFactory.__date_check(date)

        return Seminar(title, date, duration, max_participant_count, place)