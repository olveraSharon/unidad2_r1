#Nombre: Sharon Michelle Olvera Ibarra
#Descripción:La clase Timer
#Fecha: 27/10/2023

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return self.format_time()

    def format_time(self):
        return f"{self.__format_value(self.__hours)}:{self.__format_value(self.__minutes)}:{self.__format_value(self.__seconds)}"

    def __format_value(self, value):
        return str(value).zfill(2)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours = (self.__hours + 1) % 24

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours = (self.__hours - 1) % 24


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
