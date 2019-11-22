from threading import Thread
import time
class ExampleThread(Thread):
    def __init__ (self, num, name):
        Thread.__init__(self)
        self.num = num
        self.name = name

    def run(self):
        for i in range(3):
            print(self.name+ " count: "  + str(i + self.num)+ "\n")
        print(self.name + " concluida!")

lista = [ExampleThread(5, "thread 1"), ExampleThread(5, "thread 2"), 
ExampleThread(5, "thread 3")]

print(lista)

for thread in lista:
    thread.start()
    thread.join()


while 1:
    time.sleep(10)
    print("programa principal")