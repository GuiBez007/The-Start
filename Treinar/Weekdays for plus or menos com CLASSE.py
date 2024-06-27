class WeekDayError(Exception):
    pass
	

class Weeker:
    __weekdays = ['Mon','Thu','Wed','Thu','Fri','Sat','Sun']

    def __init__(self, day):
        try:
            self.__day = Weeker.__weekdays.index(day)
        except:
            raise WeekDayError

    def __str__(self):
        return Weeker.__weekdays[self.__day]

    def add_days(self, n):
        self.__day = self.__day + n
        while self.__day > 6:
            self.__day = self.__day - 7

    def subtract_days(self, n):
        self.__day = self.__day - n
        while self.__day < 0:
            self.__day = 7 + self.__day

#OBS: a form of upgrade these methods, it's swith the 'while' for 'self.__day = (self.__day - n) % 7' being 7 the lenght of a specific list


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

input()
