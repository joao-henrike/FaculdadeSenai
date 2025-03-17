#include <stdio.h>
#include <stdlib.h>

int main() {
    int **lista = malloc(10 * sizeof(int*)), valor = 100;

    for (int i = 0; i < 10; i++) {
        lista[i] = malloc(10 * sizeof(int));
        for (int j = 0; j < 10; j++)
            lista[i][j] = valor--;
    }

    for (int i = 9; i >= 0; i--) {
        for (int j = 9; j >= 0; j--)
            printf("%3d ", lista[i][j]);
        printf("\n");
        free(lista[i]);
    }
    free(lista);

    return 0;
}
