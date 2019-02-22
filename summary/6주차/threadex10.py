import threading

sem = threading.Semaphore(3)

class RestrictedArea(threading.Thread):
    def run(self):
        for x in range(500):
            # before stuff
            sem.acquire()
            # do something...
            # print('do something...')
            sem.release()
            # after stuff

thlist = []

# 100개의 쓰레드 생성
for i in range(100):
    thlist.append(RestrictedArea())

for th in thlist:
    th.start()

for th in thlist:
    th.join()

print('exiting')