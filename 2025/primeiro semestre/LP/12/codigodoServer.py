import socket
import sys
import os

# Lê o arquivo de configuração
def read_config():
    config = {}
    if os.path.exists('config.txt'):
        with open('config.txt', 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                config[key] = value
    else:
        print("Arquivo de configuração não encontrado!")
        sys.exit(1)
    return config

def start_server():
    config = read_config()
    host = config.get('host', '127.0.0.1')
    port = int(config.get('port', 12345))

    # Criação do socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor aguardando conexão em {host}:{port}...")

    # Aceita uma conexão
    client_socket, client_address = server_socket.accept()
    print(f"Conectado a {client_address}")

    while True:
        # Recebe mensagem do cliente
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Mensagem do cliente: {message}")

        # Envia resposta
        response = input("Digite sua resposta: ")
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

if __name__ == '__main__':
    start_server()
