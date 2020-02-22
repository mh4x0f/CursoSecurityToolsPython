
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clientes= {}
address = {}


HOST = ''
PORT = 3000
BUFSIZE  = 1024
ADDR = (HOST, PORT)


SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def aceitar_clientes():
    while True:
        client , client_addr = SERVER.accept()
        print("{} : {} foi conetactado com sucesso".format(client_addr[0], client_addr[1]))
        client.send(bytes("Seja bem vindo ao chat!!, digite seu nome: ", 'utf8'))
        address[client] = client_addr
        Thread(target=handler_client, args=(client, )).start()



def handler_client(client):
    name = client.recv(BUFSIZE).decode("utf8")
    bemvindo = 'Seja bem-vindo {} ao chat!, digite  !quit para sair'.format(name)
    client.send(bytes(bemvindo, 'utf8'))

    broadcast(bytes("{} acabou de entrar no chat!".format(name), 'utf8'))
    clientes[client] = name
    
    while True:
        msg = client.recv(BUFSIZE).decode('utf8')
        if not '!quit' in msg:
            broadcast(bytes(msg, 'utf8'), name+ ': ')
        else:
            client.send(bytes('!quit', 'utf8'))
            client.close()
            del clientes[client]
            broadcast(bytes(" O cliente {} saiu do chat!".format(name), 'utf8'))



def broadcast(msg, prefix=""):
    for sock in clientes:
        sock.send(bytes(prefix, 'utf8') + msg)


if __name__ == '__main__':
    SERVER.listen(5)
    print('esperando clientes')
    ACCEPT_THREAD = Thread(target=aceitar_clientes)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

