#Nombre: Sharon Michelle Olvera Ibarra
#Descripción: Pila Contadora
#Fecha: 25/10/2023


class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.__counter = 0  # Inicializar el contador en cero en el constructor de la subclase

    def get_counter(self):
        return self.__counter  # Devuelve el valor actual del contador

    def pop(self):
        self.__counter += 1  # Incrementa el contador cada vez que se hace un pop
        super().pop()  # Llama al método pop de la clase base


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())  # Debería imprimir 100