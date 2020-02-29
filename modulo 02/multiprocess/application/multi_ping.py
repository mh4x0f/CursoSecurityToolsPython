from multiprocessing import Process, Pipe
import os

def create_new_process(pipe):
    print("Filho process id: {}".format(os.getpid()))
    command = pipe.recv()
    pipe.send(os.popen(command).read())
    pipe.close()

if __name__ == '__main__':
    print("Pai process id: {}".format(os.getpid()))
    saida_pai, saida_filho = Pipe()
    filho = Process(target=create_new_process, args=(saida_filho,))
    filho.start()
    saida_pai.send("ping -c1 google.com")
    print("output: {}".format(saida_pai.recv()))

    filho.join()
    print("exit...")