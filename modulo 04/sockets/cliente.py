import socket


ip = input("Digite o ip: ")
port = 7000

endereco = (ip, port)

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(endereco)


msg = input("Digite sua mensagem: ")

cliente_socket.send(msg.encode())
print("message envida com sucesso !")
cliente_socket.close()