import threading, time
import random

NR_CONSUMER = 10
NR_PRODUCER = round(NR_CONSUMER / 2)

buffer = []
cv = threading.Condition()

# 소비자
class Consumer(threading.Thread):
    def run(self):
        for x in range(5):
            cv.acquire()
            while len(buffer) < 1:
                print('waiting...')
                cv.wait()
            print(buffer.pop(0)) # 정보 소비
            cv.release()
            time.sleep(0.1) # 잠시 대기

# 생산자
class Producer(threading.Thread):
    def run(self):
        for x in range(10):
            cv.acquire()
            buffer.append(random.randrange(0, 20))
            cv.notify()
            cv.release()
            time.sleep(0.2)

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

print('Exiting', buffer)