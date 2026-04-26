from classes.course import Course
from classes.data_time import DateTim
from factories.date_time_factory import DateTimeFactory

class CourseFactory:
    @staticmethod
    def create_course(title: str, date: str, duration: str, max_participant_count: str, place: str) -> Course:
        if not duration.strip():
            raise ValueError('duration can not be empty')
        if not max_participant_count.strip():
            raise ValueError('max participant count can not be empty')

        max_participant_count = int(max_participant_count)
        duration = int(duration)
        title = title.strip()

        if not title:
            raise ValueError('title can not be empty')
        if not place.strip():
            raise ValueError('place can not be empty')
        if duration <= 0:
            raise ValueError('duration need to be higher than 0')
        if max_participant_count <= 0:
            raise ValueError('max participant count need to be higher than 0')

        datetime: DateTim = DateTimeFactory.create_date_time(date.strip())


        #it could be updated(fixed)
        persons: dict[str, list[str]] = {'participant' : [], 'docent' : []}
        max_count: dict[str, int] = {'participant' : max_participant_count, 'docent' : 2}

        return Course(title, datetime, duration, place.strip(), persons, max_count)