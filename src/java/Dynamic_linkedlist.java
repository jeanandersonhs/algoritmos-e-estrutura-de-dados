public class Dynamic_linkedlist {

    public static void main(String[] args) {
        Linkedlist linkedlist1 = new Linkedlist();


        linkedlist1.inserir_no_final(1);
        linkedlist1.inserir_no_final(100);
        linkedlist1.inserir_no_final(1000);
        linkedlist1.inserir_no_final(10000);
        linkedlist1.imprimirLinkedlist();
        linkedlist1.remover_value(1);
        linkedlist1.imprimirLinkedlist();
    }


}



class Node{

    private int valor;
    private Node proximo;

    public Node(int value){
        this.valor = value;
        this.proximo = null;
    }

    public int getValor(){
        return valor;
    }
    public void setValor(int value){
        this.valor = value;
    }

    public Node getProximo(){
        return proximo;
    }

    public void setProximo(Node prox){
        this.proximo= prox;
    }



}




class Linkedlist{
    private Node inicio = null;
    private Node rabo = null;


    public void inserir_no_final(int value){
        Node newNode = new Node(value);

        if (this.inicio == null){
            this.inicio = newNode;
            this.rabo = newNode;
        }else{
            this.rabo.setProximo(newNode);
            this.rabo = newNode;

        }



    }



    public void remover_value(int valueBuscado){
        Node atualNode = this.inicio;
        Node anteriorNode = null;



        while(atualNode != null){
            if(atualNode.getValor() == valueBuscado){
                //encontrei na lista
                //
                if (atualNode.getValor() == this.inicio.getValor()){
                    this.inicio = atualNode.getProximo();
                    atualNode.setProximo(null);
                }else{
                    anteriorNode.setProximo(atualNode.getProximo());
                    atualNode.setProximo(null);
                }
            }
            anteriorNode = atualNode;
            atualNode = atualNode.getProximo();

        }
    }


    public void imprimirLinkedlist(){
        System.out.println("-----------Imprirmindo a lista---------");

        Node atualNode = this.inicio;

        while (atualNode != null)
        {
            System.out.print(atualNode.getValor()+"-->");
            atualNode = atualNode.getProximo();
        }
        System.out.println();

    }



}
