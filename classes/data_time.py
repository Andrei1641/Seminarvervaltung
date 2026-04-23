class DateTim:
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        '''YYYY-MM-DD-HH-MM-SS'''

        self.__year: int = year
        self.__month: int = month
        self.__day: int = day
        self.__hour: int = hour
        self.__minute: int = minute
        self.__second: int = second


    def __str__(self) -> str:
        return f'{self.__year}-{self.__month}-{self.__day}-{self.__hour}-{self.__minute}-{self.__second}'


    def __eq__(self, other: 'DateTim') -> bool:
        if not isinstance(other, DateTim):
            raise TypeError('Cannot compare DateTime with non-DateTime object')

        return ((self.__year, self.__month, self.__day, self.__hour, self.__minute, self.__second) ==
                (other.__year, other.__month, other.__day, other.__hour, other.__minute, other.__second))


    def __lt__(self, other: 'DateTim') -> bool:
        if not isinstance(other, DateTim):
            raise TypeError('Cannot compare DateTime with non-DateTime object')

        return ((self.__year, self.__month, self.__day, self.__hour, self.__minute, self.__second) <
                (other.__year, other.__month, other.__day, other.__hour, other.__minute, other.__second))


    def add_time(self, *,years: int = 0, months: int = 0, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.__second = (self.__second + seconds) % 60
        self.__minute = (self.__minute + minutes + (seconds // 60)) % 60
        self.__hour = (self.__hour + hours + (minutes // 60)) % 24

        m: list[int] = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        cur_mon = (self.__month + months) % 12
        self.__year = (self.__year + years) + (self.__month + months) // 12

        days = days + hours // 24
        while days > m[cur_mon - 1]:
            days = days - m[cur_mon - 1]
            cur_mon += 1
            if cur_mon > 12:
                cur_mon = 1
                self.__year += 1

        self.__day = self.__day + days
        self.__month = cur_mon