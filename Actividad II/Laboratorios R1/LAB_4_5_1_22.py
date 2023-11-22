#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Histograma de frecuencia de caracteres
#Fecha: 20/11/2023

from datetime import datetime

# Crear un objeto datetime para el 4 de noviembre de 2020, 14:53:00
fecha_hora = datetime(2020, 11, 4, 14, 53, 0)

# Imprimir resultados con diferentes formatos
print(fecha_hora.strftime("%Y/%m/%d %H:%M:%S"))  # 2020/11/04 14:53:00
print(fecha_hora.strftime("%y/%B/%d %H:%M:%S %p"))  # 20/November/04 14:53:00 PM
print(fecha_hora.strftime("%a, %Y %b %d"))  # Wed, 2020 Nov 04
print(fecha_hora.strftime("%A, %Y %B %d"))  # Wednesday, 2020 November 04
print(f"Día de la semana: {fecha_hora.strftime('%w')}")  # Día de la semana: 3
print(f"Día del año: {fecha_hora.strftime('%j')}")  # Día del año: 309
print(f"Número de semana en el año: {fecha_hora.strftime('%U')}")  # Número de semana en el año: 44
