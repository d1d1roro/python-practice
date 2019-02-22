import threading

g_count = 0

class MyThread(threading.Thread):
    def run(self):
        global g_count
        for i in range(10):
            lock.acquire()
            g_count += 1
            lock.release()

lock = threading.Lock()
threads = []
for i in range(2):
    th = MyThread()
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print('Exiting ', g_count)