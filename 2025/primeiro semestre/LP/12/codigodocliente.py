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

def start_client():
    config = read_config()
    host = config.get('host', '127.0.0.1')
    port = int(config.get('port', 12345))

    # Criação do socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        # Envia mensagem
        message = input("Digite sua mensagem: ")
        client_socket.send(message.encode('utf-8'))

        # Recebe resposta
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Resposta do servidor: {response}")

    client_socket.close()

if __name__ == '__main__':
    start_client()
