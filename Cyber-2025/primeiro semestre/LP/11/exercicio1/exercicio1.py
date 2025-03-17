import sys

# Verifica se pelo menos dois argumentos foram passados (arquivo + pelo menos um parâmetro)
if len(sys.argv) < 3:
    print("Uso: python script.py <nome_do_arquivo> <param1> <param2> ...")
    sys.exit(1)

# Obtém o nome do arquivo
arquivo_nome = sys.argv[1]

# Obtém os parâmetros restantes
parametros = sys.argv[2:]

# Escreve os parâmetros no arquivo, cada um em uma linha
with open(arquivo_nome, "w") as file:
    for parametro in parametros:
        file.write(parametro + "\n")

print(f"Os parâmetros foram escritos em '{arquivo_nome}'.")
