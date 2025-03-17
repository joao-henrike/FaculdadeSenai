import sys

# Lê o arquivo config.txt
with open("config.txt", "r") as file:
    config = file.read().strip()

# Extrai o valor de "num" do arquivo
try:
    num = int(config.split('=')[1])
except ValueError:
    print("Erro: o formato de config.txt está incorreto!")
    sys.exit(1)

# Verifica se o número de parâmetros passados está correto
if len(sys.argv) - 1 != num:
    print(f"Erro: o número de parâmetros deve ser {num}.")
    sys.exit(1)

print(f"Parâmetros recebidos: {sys.argv[1:]}")
