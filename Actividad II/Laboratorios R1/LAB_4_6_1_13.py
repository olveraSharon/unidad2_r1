#Autor: Sharon Michelle Olvera Ibarra
#Descripción:El módulo calendar
#Fecha: 21/11/2023

from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        """
        Counts the number of occurrences of a weekday in a year.
        
        Parameters:
            year (int): The year to check.
            weekday (int): The day of the week to count (0 = Monday, 1 = Tuesday, ..., 6 = Sunday).
        
        Returns:
            int: The number of occurrences of the specified weekday in the year.
        """
        if not (0 <= weekday <= 6):
            raise ValueError("weekday must be a number between 0 and 6.")
        
        return sum(1 for month in range(1, 13) for _, weekdays in self.monthdays2calendar(year, month) for day in weekdays if day[weekday] != 0)

calendar = MyCalendar()

print(calendar.count_weekday_in_year(2019, 0)) 
print(calendar.count_weekday_in_year(2000, 6))
