#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int valor;
    struct Node* prox;
} Node;

void inserir(Node** head, int valor) {
    Node* novo = (Node*)malloc(sizeof(Node));
    novo->valor = valor;
    novo->prox = *head;
    *head = novo;
}

void imprimir(Node* head) {
    while (head) {
        printf("%d ", head->valor);
        head = head->prox;
    }
}

int main() {
    Node* lista = NULL;

    for (int i = 20; i >= 11; i--)
        inserir(&lista, i);

    imprimir(lista);

    return 0;
}
