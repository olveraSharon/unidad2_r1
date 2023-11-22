#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Histograma de frecuencia de caracteres ordenado
#Fecha: 20/11/2023

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

# Ordenar el histograma por frecuencia de caracteres
sorted_histogram = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

# Imprime y escribir en el archivo '.hist'
hist_filename = filename.split('.')[0] + '.hist'
with open(hist_filename, 'w') as hist_file:
    print("Histograma de letras:")
    for letter, count in sorted_histogram:
        if count > 0:
            print(f"{letter} -> {count}")
            hist_file.write(f"{letter} -> {count}\n")

print(f"El histograma ha sido guardado en {hist_filename}.")
