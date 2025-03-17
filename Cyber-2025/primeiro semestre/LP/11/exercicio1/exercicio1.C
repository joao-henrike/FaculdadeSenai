#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Verifica se pelo menos dois argumentos foram passados (arquivo + pelo menos um parâmetro)
    if (argc < 3) {
        printf("Uso: ./script <nome_do_arquivo> <param1> <param2> ...\n");
        return 1;
    }

    // Obtém o nome do arquivo
    char *arquivo_nome = argv[1];

    // Abre o arquivo para escrita
    FILE *file = fopen(arquivo_nome, "w");
    if (!file) {
        printf("Erro ao abrir o arquivo %s\n", arquivo_nome);
        return 1;
    }

    // Escreve os parâmetros no arquivo, cada um em uma linha
    for (int i = 2; i < argc; i++) {
        fprintf(file, "%s\n", argv[i]);
    }

    fclose(file);
    printf("Os parâmetros foram escritos em '%s'.\n", arquivo_nome);

    return 0;
}
