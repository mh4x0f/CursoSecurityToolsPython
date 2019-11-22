import threading, time
import queue as Queue

class ThreadTarde(threading.Thread):
    def __init__(self, queue, max_time):
        threading.Thread.__init__(self)
        self.count = None
        self.max  = max_time
        self.q = queue
    
    def run(self):
        while (not self.count):
            while not self.q.empty():
                self.count = self.q.get()
                break

        print("[*] Iniciando Trabalho do segundo turno.")
        print("[*] Objetivo: " + str(self.count) + "/"+ str(self.max))
        for i in range(self.count, int(self.max +1)):
            time.sleep(3)
            print("Thread Tarde: working count: " + str(i))
        print("[*] Trabalho concluido! ")

class ThreadManha(threading.Thread):
    def __init__(self, queue, max_time):
        threading.Thread.__init__(self)
        self.count = None
        self.max  = int(max_time/2)
        self.q = queue
    
    def run(self):
        self.count = 0
        print("[*] Iniciando Trabalho do primeiro turno.")
        print("[*] Objetivo: " + str(self.count) + "/"+ str(self.max))
        for i in range(self.count, int(self.max)):
            time.sleep(3)
            print("Thread Manha: working count: " + str(i))
        self.q.put(self.max)

q = Queue.Queue()

thread_1  = ThreadManha(q, 10)
thread_2  = ThreadTarde(q,10)

thread_1.start()
thread_2.start()
