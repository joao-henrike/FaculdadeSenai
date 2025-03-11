#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <dirent.h>

void criar_diretorio(const char *nome) {
    mkdir(nome, 0777) == 0 ? printf("Diretório '%s' criado.\n", nome) : perror("Erro");
}

void listar_diretorio(const char *nome) {
    DIR *dir = opendir(nome);
    if (!dir) { perror("Erro"); return; }

    struct dirent *entrada;
    while ((entrada = readdir(dir))) printf("%s\n", entrada->d_name);
    closedir(dir);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s <criar|listar> <diretório>\n", argv[0]);
        return 1;
    }
    
    !strcmp(argv[1], "criar") ? criar_diretorio(argv[2]) :
    !strcmp(argv[1], "listar") ? listar_diretorio(argv[2]) :
    printf("Comando inválido!\n");

    return 0;
}
