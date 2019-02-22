import threading, time

def myThread(id):
    for i in range(10):
        print('id %s --> %s' % (id, i))
        time.sleep(0) # cpu 양도

threads = []

for i in range(2):
    th = threading.Thread(target=myThread, args=(i,)) # args 튜플 형태로 넘김
    th.start() # run 메서드 호출해줌
    threads.append(th)

for th in threads:
    th.join() # 각 쓰레드가 끝날 때까지 대기

print('exiting')