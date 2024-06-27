def transformador(hour,minute,second):
    if len(str(hour)) < 2:
        hour = "0" + str(hour)
    if len(str(minute)) < 2:
        minute = "0" + str(minute)
    if len(str(second)) < 2:
        second = "0" + str(second)
    return str(hour) + ':' + str(minute) + ':' + str(second)

class Timer:
    def __init__(self,hour=0,minute=0,second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return transformador(self.__hour,self.__minute,self.__second)

    def next_second(self):
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0
                    self.__minute = 0
                    self.__second = 0
        

    def prev_second(self):
        self.__second -= 1
        if self.__second == -1:
            self.__second = 59
            self.__minute -= 1
            if self.__minute == -1:
                self.__minute = 59
                self.__hour -= 1
                if self.__hour == -1:
                    self.__hour = 23
                    self.__minute = 59
                    self.__second = 59

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
input()
