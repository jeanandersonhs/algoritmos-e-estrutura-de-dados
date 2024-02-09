import gc
import numpy as np

class Node:
    def __init__(self, value):
        self.valor = value
        self.proximo = None
    
    def getValor(self):
        return self.valor


class Queue:
    #FIFO 
    def __init__(self):
            self.inicio = None
            self.cauda = None
    

    def enfileirar(self, valueInsercao):
        node = Node(valueInsercao)
        

        if self.inicio:
            atualFim = self.cauda

            atualFim.proximo = node
            self.cauda = node
            return

        self.inicio = node
        self.cauda = node


    def desenfileirar(self):

        if self.inicio :

            atualInicio = self.inicio

            self.inicio = atualInicio.proximo

            del atualInicio
            gc.collect()

    
    def imprimirQueue(self):
        atual = self.inicio

        while atual:
            print(f'{atual.getValor()}')
            atual = atual.proximo

        return 
    

def main():
    novaFila = Queue()

    novaFila.enfileirar(1)

    novaFila.enfileirar(10)
    novaFila.enfileirar(1000)
    novaFila.enfileirar(10000)
    novaFila.enfileirar(100000)
    novaFila.imprimirQueue()
    print("-----------")
    novaFila.desenfileirar()
    novaFila.imprimirQueue()




if __name__ =="__main__":
    main()






