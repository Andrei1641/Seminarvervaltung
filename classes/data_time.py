class DateTim:
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        '''YYYY-MM-DD-HH-MM-SS'''

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second


    def __str__(self) -> str:
        return f'{self.year}-{self.month}-{self.day}-{self.hour}-{self.minute}-{self.second}'

    def __lt__(self, other: 'DateTim') -> bool:
        if not isinstance(other, DateTim):
            raise TypeError('Cannot compare DateTime with non-DateTime object')

        return ((self.year, self.month, self.day, self.hour, self.minute, self.second) <
                (other.year, other.month, other.day, other.hour, other.minute, other.second))


    def add_time(self, *,years: int = 0, months: int = 0, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.second = (self.second + seconds) % 60
        self.minute = (self.minute + minutes + (seconds // 60)) % 60
        self.hour = (self.hour + hours + (minutes // 60)) % 60

        m: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        cur_mon = (self.month + months) % 12
        self.year = (self.year + years) + (self.month + months) // 12

        while days > m[cur_mon - 1]:
            days = days - m[cur_mon - 1]
            cur_mon += 1
            if cur_mon > 12:
                cur_mon = 1
                self.year += 1

        self.month = cur_mon