import _thread, time

NoOfThread = 5
threadexit = [0] * NoOfThread

def counter(id, count):
    for i in range(count):
        print('id %s --> %s' % (id, i))
    threadexit[id] = 1

for i in range(NoOfThread):
    _thread.start_new_thread(counter, (i, 5))

while 0 in threadexit:
    time.sleep(0.1)

print('Exiting', threadexit)
