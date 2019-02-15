from telnetlib import Telnet
import getpass

def telnetClient(host):
    telnet = Telnet(host)
    telnet.read_until(b'login:')

    user = input("Enter your remote account:")
    telnet.write((user+'\n').encode('utf-8'))
    telnet.read_until(b'Password:')
    password = getpass.getpass()
    telnet.write((password+'\n').encode('utf-8'))
    cmd = input("Enter your command:")
    telnet.write((cmd+'\n').encode('utf-8'))
    telnet.write(b'exit\n')
    return telnet.read_all()

if __name__ == '__main__':
    r = telnetClient('3.17.61.134')
    print(r)