from telnetlib import Telnet
import sys

class TelnetClient:
    def __init__(self, host):
        self.telnet = Telnet(host)

    def mt_interact(self):
        import threading
        threading._start_new_thread(self.listener, ())
        while 1:
            line = sys.stdin.readline()
            if not line:
                break
            self.telnet.write(line.encode('utf-8'))
    
    def listener(self):
        while 1:
            try:
                data = self.telnet.read_eager()
            except EOFError:
                print('*** Connection closed by remote host ***')
                return

            if data:
                sys.stdout.write(str(data))
            else:
                sys.stdout.flush()

if __name__ == '__main__':
    tc = TelnetClient('3.17.61.134')
    tc.mt_interact()