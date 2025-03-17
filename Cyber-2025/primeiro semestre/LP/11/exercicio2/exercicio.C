#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CONFIG_FILE "config.txt"

int main(int argc, char *argv[]) {
    FILE *file = fopen(CONFIG_FILE, "r");
    if (!file) {
        printf("Erro: Não foi possível abrir o arquivo %s\n", CONFIG_FILE);
        return 1;
    }

    int num;
    if (fscanf(file, "num=%d", &num) != 1) {
        printf("Erro: O formato de config.txt está incorreto!\n");
        fclose(file);
        return 1;
    }
    fclose(file);

    // Verifica se o número de parâmetros está correto
    if (argc - 1 != num) {
        printf("Erro: O número de parâmetros deve ser %d.\n", num);
        return 1;
    }

    printf("Parâmetros recebidos: ");
    for (int i = 1; i < argc; i++) {
        printf("%s ", argv[i]);
    }
    printf("\n");

    return 0;
}
