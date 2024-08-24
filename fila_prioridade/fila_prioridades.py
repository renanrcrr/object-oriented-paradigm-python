import heapq

class FilaDePrioridade:
    def __init__(self):
        self.fila = []
        self.indice = 0
    
    def inserir(self, item, prioridade):
        # heappush adiciona item a uma fila
        heapq.heappush(self.fila, (-prioridade, self.indice, item))
        self.indice += 1

    def remover(self):
        # heappop remove item da fila
        return heapq.heappop(self.fila)[-1]
    
class Item:
    def __init__(self, nome):
        self.nome = nome
    
    def __repr__(self):
        return self.nome
    
fila = FilaDePrioridade()
fila.inserir(Item('renan'), 38)
fila.inserir(Item('patrick'), 37)
fila.inserir(Item('diego'), 42)

print(fila.remover())
