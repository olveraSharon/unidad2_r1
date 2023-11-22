#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Un Display LED
#Fecha: 18/11/2023

def imprimir_numero(numero):
    # Definir los patrones para cada dígito
    patrones = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"]   # 9
    ]

    # Convertir el número a una lista de dígitos
    digitos = [int(digito) for digito in str(numero)]

    # Imprimir cada línea del display
    for i in range(5):
        for digito in digitos:
            print(patrones[digito][i], end="   ")
        print()

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número no negativo: "))
imprimir_numero(numero)
