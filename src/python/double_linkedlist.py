import gc
import numpy as np
class Node:
    def __init__(self, value):
        self.proximo = None
        self.anterior = None
        self.valor = value
    
    def imprimir_node(self):
        return self.valor


class Linkedlist:
    def __init__(self):
        self.cabeca = None


    #inserindo
    def inserir_no_final(self,value_node):
        node = Node(value_node)
        
        if self.cabeca:
            atual = self.cabeca

            while atual.proximo:
                atual = atual.proximo
            
            atual.proximo = node
            node.anterior = atual
            return

        if self.cabeca ==None:
            self.cabeca = node
            return

    def remover_no_final(self):
        
        if self.cabeca:
            atual = self.cabeca

            while atual.proximo:
                anterior = atual
                atual = atual.proximo

            anterior.proximo = None
            del atual
            gc.collect()

    def imprimirAnteriorDoUltimo(self):
        if self.cabeca:
            atual =self.cabeca

            while atual.proximo:
                atual = atual.proximo

            print(atual.anterior.valor)


    def imprimir_lista(self):

        if self.cabeca:
            #imprimindo a lista
            atual = self.cabeca
            while atual:
                print(atual.imprimir_node(), end=" ")
                atual = atual.proximo
            return
                
        print("a lista esta vazia")
 
def main():
    print("insirar um valor na lista")
    lista1 = Linkedlist()
    entrada = input()
    vetor1 = np.array(list(map(int, entrada.split())))


    for i in np.arange(10):
        lista1.inserir_no_final(vetor1[i])
    
    lista1.imprimir_lista()
    lista1.remover_no_final()
    print()
    lista1.imprimir_lista()
    print("anterior do ultimo")
    lista1.imprimirAnteriorDoUltimo()
if __name__== "__main__":
    main()

