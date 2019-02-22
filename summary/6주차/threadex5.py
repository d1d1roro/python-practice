import _thread, time

NoOfThread = 5
ThreadLeft = NoOfThread
lock = _thread.allocate_lock()

def threadexit(id):
    global ThreadLeft
    print('thread %d is quitting' % id)
    lock.acquire()
    ThreadLeft -= 1

    lock.release()

def counter(id, count):
    for i in range(count):
        print('id %s --> %s' % (id, i))
    threadexit(id)

for i in range(NoOfThread):
    _thread.start_new_thread(counter, (i, 5))

while ThreadLeft:
    time.sleep(0.1)

print('Exiting')