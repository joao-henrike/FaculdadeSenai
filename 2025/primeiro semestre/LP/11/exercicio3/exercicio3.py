import sys
import configparser

# Lê o número de arquivos a partir do config.txt
config = configparser.ConfigParser()
config.read("config.txt")

try:
    num_arquivos = int(config["DEFAULT"]["num"])
except (KeyError, ValueError):
    print("Erro: O formato de config.txt está incorreto!")
    sys.exit(1)

# Verifica se a quantidade correta de arquivos foi passada
if len(sys.argv) - 1 != num_arquivos:
    print(f"Erro: O número de arquivos deve ser {num_arquivos}.")
    sys.exit(1)

# Cria/abre "resultado.txt" para escrita
with open("resultado.txt", "w") as resultado:
    for nome_arquivo in sys.argv[1:]:
        try:
            with open(nome_arquivo, "r") as arquivo:
                resultado.write(arquivo.read() + "\n")  # Escreve o conteúdo no arquivo de saída
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado!")
            sys.exit(1)

print("Os arquivos foram mesclados em 'resultado.txt'.")
