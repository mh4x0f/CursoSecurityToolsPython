from threading import Thread
import time
class ExampleThread(Thread):
    def __init__ (self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        for i in range(10):
            print(i + self.num)

a = ExampleThread(5)
a.start() 
print("executando fora da thread")
a.join()
print("continuando o codigo")
