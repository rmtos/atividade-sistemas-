import socket

def process_message(message):
    # Implemente a lógica para processar o comando recebido do cliente
    # Neste exemplo, o servidor simplesmente converte o texto em maiúsculas
    return message.upper()

def start_server():
    host = '127.0.0.1'  # Endereço IP do servidor
    port = 12345  # Porta para escutar as conexões

    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket ao endereço e porta especificados
    server_socket.bind((host, port))

    # Escuta por conexões recebidas
    server_socket.listen(1)

    print('Servidor pronto para receber conexões...')

    while True:
        # Aceita uma nova conexão
        client_socket, addr = server_socket.accept()

        print('Conexão estabelecida com', addr)

        # Recebe a mensagem do cliente
        message = client_socket.recv(1024).decode()

        # Processa a mensagem
        response = process_message(message)

        # Envia a resposta de volta para o cliente
        client_socket.send(response.encode())

        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == '__main__':
    start_server()

#Escrever o código do cliente

import socket

def send_message(message):
    host = '127.0.0.1'  # Endereço IP do servidor
    port = 12345  # Porta para se conectar ao servidor

    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect((host, port))

    # Envia a mensagem para o servidor
    client_socket.send(message.encode())

    # Recebe a resposta do servidor
    response = client_socket.recv(1024).decode()

    # Imprime a resposta
    print('Resposta do servidor:', response)

    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == '__main__':
    message = input('Digite uma mensagem para enviar ao servidor: ')
    send_message(message)

    # Executar e testar a comunicação
    print('Execute')

    # Ao executar o cliente, ele irá solicitar que você digite uma mensagem.
    print('Digite a mensagem')

    # Implementar recursos adicionais e testes de eficiência aplicando cliente-servidor básica funcionando, você pode implementar recursos adicionais, como autenticação de usuário, criptografia de mensagens ou qualquer outra funcionalidade específica do seu projeto.
    print('Implemente')

    # Documentar o código desenvolvido incluindo comentários explicativos em cada trecho relevante. 
    print('Documentar o codigo')

    