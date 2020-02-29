from multiprocessing import Process, Pipe
import os

def f(conn):
    print("main process")
    print(os.getpid())
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    print("main app")
    print(os.getpid())
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()