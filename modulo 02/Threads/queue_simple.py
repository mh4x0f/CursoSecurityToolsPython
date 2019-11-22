from threading import Thread
import time
import queue

class ExampleThread(Thread):
    def __init__ (self, num, name):
        Thread.__init__(self)
        self.num = num
        self.name = name
        self.status = True

    def run(self):
        for i in range(3):
            time.sleep(0.1)
            print(self.name+ " count: "  + str(i + self.num)+ "\n")
        print(self.name + " concluida!")
        self.status = False

q = queue.Queue()

lista = [ExampleThread(5, "thread 1"), ExampleThread(5, "thread 2"), 
ExampleThread(5, "thread 3")]

for thread in lista:
    q.put(thread)
    
while not q.empty():
    thread = q.get()
    thread.start()
    while(thread.status):
        pass
