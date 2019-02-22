import threading
import time
import random
from queue import Queue

NR_CONSUMER = 10
NR_PRODUCER = round(NR_CONSUMER / 2)

que = Queue(10)

class Consumer(threading.Thread):
    def run(self):
        for i in range(5):
            print(que.get())
            time.sleep(0)
class Producer(threading.Thread):
    def run(self):
        for i in range(10):
            que.put(random.randint(0, 20))
            time.sleep(0)
con = []
pro = []

for i in range(NR_CONSUMER):
    con.append(Consumer())

for i in range(NR_PRODUCER):
    pro.append(Producer())

for th in con:
    th.start()

for th in pro:
    th.start()

for th in con:
    th.join()

for th in pro:
    th.join()

print('exiting')