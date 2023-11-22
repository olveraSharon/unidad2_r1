#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Histograma de frecuencia de caracteres
#Fecha: 18/11/2023

filename = input("Introduce el nombre del archivo: ")

try:
    with open(filename, "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f"El archivo {filename} no se pudo encontrar.")
    exit()

letter_counts = {}

for letter in content:
    if letter.isalpha():
        letter = letter.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

print("Histograma de letras:")
for letter in sorted(letter_counts):
    count = letter_counts[letter]
    if count > 0:
        print(f"{letter} -> {count}")


