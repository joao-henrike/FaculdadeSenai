#include <stdio.h>
#include <stdlib.h>

#define CONFIG_FILE "config.txt"
#define OUTPUT_FILE "resultado.txt"

int main(int argc, char *argv[]) {
    // Lê o número de arquivos a partir do config.txt
    FILE *config = fopen(CONFIG_FILE, "r");
    if (!config) {
        printf("Erro: Não foi possível abrir o arquivo %s\n", CONFIG_FILE);
        return 1;
    }

    int num_arquivos;
    if (fscanf(config, "num=%d", &num_arquivos) != 1) {
        printf("Erro: O formato de config.txt está incorreto!\n");
        fclose(config);
        return 1;
    }
    fclose(config);

    // Verifica se a quantidade correta de arquivos foi passada
    if (argc - 1 != num_arquivos) {
        printf("Erro: O número de arquivos deve ser %d.\n", num_arquivos);
        return 1;
    }

    // Cria/abre "resultado.txt" para escrita
    FILE *resultado = fopen(OUTPUT_FILE, "w");
    if (!resultado) {
        printf("Erro: Não foi possível criar o arquivo %s\n", OUTPUT_FILE);
        return 1;
    }

    // Lê o conteúdo dos arquivos e escreve em "resultado.txt"
    for (int i = 1; i < argc; i++) {
        FILE *arquivo = fopen(argv[i], "r");
        if (!arquivo) {
            printf("Erro: Arquivo '%s' não encontrado!\n", argv[i]);
            fclose(resultado);
            return 1;
        }

        char linha[1024];  // Buffer para leitura
        while (fgets(linha, sizeof(linha), arquivo)) {
            fputs(linha, resultado);
        }
        fputs("\n", resultado); // Adiciona uma quebra de linha entre arquivos
        fclose(arquivo);
    }

    fclose(resultado);
    printf("Os arquivos foram mesclados em '%s'.\n", OUTPUT_FILE);

    return 0;
}
