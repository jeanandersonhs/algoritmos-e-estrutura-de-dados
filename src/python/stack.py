import gc
import numpy as np

class Node:
    def __init__(self, value):
        self.proximo = None
        self.valor = value
    
    def getValor(self):
        return self.valor


class Stack:
    def __init__(self):
        self.topo = None
            
    #politica de escrita
    #LIFO(last in, first out)


    def empilhar_push(self,value_node):
        node = Node(value_node)
        
        if self.topo is None:
            self.topo = node
            return
        
        node.proximo = self.topo
        self.topo = node
            
        

    def delete_pop(self):
        
        if self.topo:
            atual = self.topo
            #atualizando o topo
            self.topo = atual.proximo

            del atual
            gc.collect()

    def imprimirPilha(self):
        if self.topo:
            atual = self.topo
            
            while atual:
                print(f'{atual.getValor()}')
                atual = atual.proximo
 
def main():
    
    newPilha = Stack()
    newPilha.empilhar_push(1)
    newPilha.empilhar_push(2)
    newPilha.empilhar_push(3)
    newPilha.empilhar_push(4)
    newPilha.empilhar_push(5)
    
    newPilha.imprimirPilha()

    newPilha.delete_pop()
    print("----------------------------------")
    newPilha.imprimirPilha()

if __name__== "__main__":
    main()

