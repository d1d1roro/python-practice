import threading

eve = threading.Event()

class PrepareThread(threading.Thread):
    def run(self):
        eve.set()
        print('Ready')
class ActionThread(threading.Thread):
    def run(self):
        print(self.getName(), 'waiting...')
        eve.wait()
        print(self.getName(), 'done')
thlist = []
for i in range(5):
    thlist.append(ActionThread())

for th in thlist:
    th.start()

PrepareThread().start()

for th in thlist:
    th.join()

print('Exiting')