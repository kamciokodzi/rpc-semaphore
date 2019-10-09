import rpyc
import time
from random import randrange

class Client:
    def __init__(self):
        self.semaphore = rpyc.connect("localhost", 18812, config={'sync_request_timeout': None})

    def lock(self, val):
        return self.semaphore.root.P(val)

    def unlock(self, val):
        return self.semaphore.root.V(val)

if __name__ == "__main__":
    client = Client()
    while True:
        val = randrange(10) + 1
        print("LOCK BY " + str(val))
        client.lock(val)
        time.sleep(1)
        print("UNLOCK BY " + str(val))
        client.unlock(val)