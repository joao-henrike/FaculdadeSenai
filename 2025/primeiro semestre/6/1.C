#include <stdio.h>

int main() {
    int vetor[10];

    for (int i = 0; i < 10; i++)
        vetor[i] = 11 + i;

    for (int i = 0; i < 10; i++)
        printf("%d ", vetor[i]);

    return 0;
}
