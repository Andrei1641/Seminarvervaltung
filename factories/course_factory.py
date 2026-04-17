from classes.course import Course
from classes.data_time import DateTim
from factories.date_time_factory import DateTimeFactory

class CourseFactory:
    @staticmethod
    def create_course(title: str, date: str, duration: int, max_participant_count: int, place: str) -> Course:

        if not title.strip():
            raise ValueError('title can not be empty')
        if not place.strip():
            raise ValueError('place can not be empty')
        if duration <= 0:
            raise ValueError('duration need to be higher than 0')
        if max_participant_count <= 0:
            raise ValueError('max participant count need to be higher than 0')

        datetime: DateTim = DateTimeFactory.create_date_time(date.strip())

        return Course(title.strip(), datetime, duration, max_participant_count, place.strip())