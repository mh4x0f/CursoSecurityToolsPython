from multiprocessing import Process, Queue, current_process
import time, os

class ModulesBase(object):
    def __init__(self,name):
        self.name = name
    
    def run(self):
        print("ProcID: {}".format(os.getpid()))
        proc_name = current_process().name
        time.sleep(3)
        print("Process: {} Process Name: {}".format(proc_name, self.name))
        print("running exploit...")

def worker(q):
    while (not q.empty()):
        obj = q.get()
        obj.run()


if __name__ == '__main__':
    queue =  Queue()


    p = Process(target=worker, args=(queue, ))
    p.start()

    queue.put(ModulesBase("Modulo base 1"))
    queue.put(ModulesBase("Modulo base 2"))

    queue.close()
    queue.join_thread()
    p.join()