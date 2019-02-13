import socket
from socketserver import ThreadingTCPServer, StreamRequestHandler
import threading

PORT = 8037
lock = threading._allocate_lock()

class Subscriber(object):
    def __init__(self, parent, name=''):
        self.parent = parent
        print('self.parent: ' + self.parent)
        self.name = name
        self.sock = parent.request
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def upload(self, msg):
        self.getParent().publisher.handleMessage(self, msg)
    def send(self, msg):
        self.parent.request.sendall(msg)
    def close(self):
        self.parent.request.shutdown(socket.SHUT_RD | socket.SHUT_WR)
        self.parent.request.close()
    def getParent(self):
        return self.parent
    
class Publisher(object):
    def __init__(self):
        self.substribers = {}
    def addUser(self, user):
        if user.getName() in self.substribers:
            user.send('이미 등록된 이름입니다.\n')
            return False
        lock.acquire()
        self.substribers[user.getName()] = user
        lock.release()
        self.broadcastMessage('[' + user.getName() + '] ' + ' 님께서 인장하셨습니다.\n')
        user.sned('[%s]님 어서오세요.\n' % user.getName())
        print('%s joined' % user.getName())
        print(len(self.substribers), 'connections')
        return True
    def removeUser(self, name):
        if name not in self.substribers:
            return False
        user = self.substribers[name]
        user.send('연결을 종료합니다.\n')
        user.close()
        user.getParent().connectedFlag = False
        lock.acquire()
        del self.substribers[name]
        lock.release()
        self.broadcastMessage('[' + name + '] 님께서 나가셨습니다.\n')
        print('%s left' % name)
        print(len(self.substribers), 'connections')
        return True
    def handleMessage(self, user, msg):
        if not msg.strip():
            return
        if not msg.startswith('/'):
            self.broadcastMessage('[' + user.getName() + '] ' + msg)
            return
        args = msg[1:].split()
        if hasattr(self, 'action_' + args[0]):
            getattr(self, 'action_' + args[0])(user.getName(), args[1:])
    def broadcastMessage(self, msg):
        for user in self.substribers.values():
            user.send(msg)
    def action_quit(self, name, args):
        return self.removeUser(name)

class ChatRequestHandler(StreamRequestHandler):
    publisher = Publisher()
    def handle(self):
        print('connection from', self.client_address)
        try:
            user = self.readAndRegisterName()
            if not user: raise Exception
            self.connectedFlag = True
            data = self.rfile.readline()
            while data:
                user.upload(data)
                if not self.connectedFlag:
                    break
                data = self.rfile.readline()
        except socket.error:
            print('Socket Error')
        except Exception:
            pass
        print('Disconnected from', self.client_address)

        try:
            self.publisher.removeUser(user.getName())
        except: pass
    
    def readAndRegisterName(self):
        user = Subscriber(self)
        while 1:
            user.send('이름을 입력해주세요: \n')
            try:
                name = self.rfile.readline().strip()
            except socket.error:
                user.close()
                return
            if not name or name.startswith('/'):
                user.send('잘못된 이름입니다.\n')
                continue
            user.setName(name)
            if self.publisher.addUser(user):
                return user

class ChatServer(ThreadingTCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    server = ChatServer(("", PORT), ChatRequestHandler)
    print('listening on port', PORT)
    server.serve_forever()
