import rpyc
from rpyc.utils.server import ThreadedServer
from multiprocessing import Lock
import time

size = 10
threadsInQueue = 0
wait = True
lock = Lock()

class Server(rpyc.Service):
    def exposed_P(self, val):
        notify = False
        global wait
        global threadsInQueue
        global lock
        global size
        while val > size and not notify:
            threadsInQueue += 1
            while wait:
                pass
            with lock:
                threadsInQueue -= 1
                if threadsInQueue == 0:
                    wait = True
            while not wait:
                pass
            with lock:
                if size >= val:
                    print("IN CS")
                    size -= val
                    notify = True
                    print("OUT OF CS")
        if not notify:
            size -= val
        print("Size after P: " + str(size))

    def exposed_V(self, val):
        global size
        global wait
        global lock
        with lock:
            size += val
            wait = False
        print("Actual size after Out is " + str(size))


if __name__ == "__main__":
    server = ThreadedServer(Server, port = 18812)
    server.start()