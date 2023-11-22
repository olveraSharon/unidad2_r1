#Nombre: Sharon Michelle Olvera Ibarra
#Descripción: Días de la semana
#Fecha: 27/10/2023

class WeekDayError(Exception):
    pass

class Weeker:
    _days_of_week = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        if day not in self._days_of_week:
            raise WeekDayError
        self._current_day = day

    def __str__(self):
        return self._current_day

    def add_days(self, n):
        current_index = self._days_of_week.index(self._current_day)
        new_index = (current_index + n) % 7
        self._current_day = self._days_of_week[new_index]

    def subtract_days(self, n):
        current_index = self._days_of_week.index(self._current_day)
        new_index = (current_index - n) % 7
        self._current_day = self._days_of_week[new_index]

try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")

