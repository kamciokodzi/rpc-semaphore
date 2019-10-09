# RPC Semaphore

## Setup

Python 2.7.16 was used to implement this project.
In addition `rpyc` library is needed.
```
> python --version
Python 2.7.16

> pip install rpyc
```

## Run
```
python Server.py
python Client.py
```

## Explanation
Clients try to take some units from semaphore by a value generated by random.

Server uses `ThreadedServer` from `rpyc` library to receive multiple connection. It's also using `Lock` from `multiprocessing` library to assure that only one thread executes given code. Thanks to that object model is implicitly safe against concurrent access.

Server checks if value given by client is lesser than actual semaphore size. If yes then it's take value and response to Client. In other case adds Client to queue and wait until someone raise semaphore. Leaves queue and waits on the barrier to synchronize with other Clients. If all Clients leave queue then they are synchronized and leaves while loop. Then every Client goes through condition if it can go in Critical Section, if yes: then it takes semaphore otherwise it goes again through whole process.
