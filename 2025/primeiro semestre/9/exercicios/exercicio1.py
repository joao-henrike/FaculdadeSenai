import os
import sys

def criar_diretorio(nome):
    os.makedirs(nome, exist_ok=True)
    print(f"Diretório '{nome}' criado.")

def listar_diretorio(nome):
    if not os.path.exists(nome):
        print(f"Erro: O diretório '{nome}' não existe.")
        return
    print("\n".join(os.listdir(nome)) if os.listdir(nome) else "Diretório vazio.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <criar|listar> <diretório>")
        sys.exit(1)

    {"criar": criar_diretorio, "listar": listar_diretorio}.get(sys.argv[1], lambda _: print("Comando inválido!"))(sys.argv[2])
