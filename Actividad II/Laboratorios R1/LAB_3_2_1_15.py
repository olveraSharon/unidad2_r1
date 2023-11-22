#Nombre: Sharon Michelle Olvera Ibarra
#Descripción: Colas alias FIFO
#Fecha: 25/10/2023

class QueueError(Exception): 
    pass

class Queue:
    def __init__(self):
        self.items = []

    def put(self, elem):
        self.items.insert(0, elem)

    def get(self):
        if len(self.items) == 0:
            raise QueueError("La cola está vacía.")
        return self.items.pop()

que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError as e:
    print("Error de Cola")
