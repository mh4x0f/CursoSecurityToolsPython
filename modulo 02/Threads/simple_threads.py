import _thread
import time




def print_time (nomedothread, delay):
    conta = 0
    while conta < 5:
        time.sleep(delay)
        conta += 1
        print("%s: %s" % (nomedothread, time.ctime(time.time()) ))

_thread.start_new_thread( print_time, ("Thread-1", 2, ) )
_thread.start_new_thread( print_time, ("Thread-2", 4, ) )

while 1:
    print("Programa principal...")
    time.sleep(10)
    pass
