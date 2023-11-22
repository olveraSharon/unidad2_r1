#Nombre: Sharon Michelle Olvera Ibarra
#Descripción: Colas alias FIFO: parte 2
#Fecha: 25/10/2023

class QueueError(Exception): 
    pass

class Queue:
    #Código anterior
    def __init__(self):
        self.items = []

    def put(self, elem):
        self.items.insert(0, elem)

    def get(self):
        if len(self.items) == 0:
            raise QueueError("La cola está vacía.")
        return self.items.pop()

    def isempty(self):
        return len(self.items) == 0


class SuperQueue(Queue):
    #Código nuevo
    def isempty(self):
        return len(self.items) == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
