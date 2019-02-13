# from socket import *
# import struct

# def dottedQuadtoNum(ip):
#     "convert decimal dotted quad string to long interger"
#     return struct.unpack('>L', inet_aton(ip))[0]

# ip = '235.5.5.5' # 그룹 주소
# mreq = struct.pack('11', htonl(dottedQuadtoNum(ip)), INADDR_ANY)
# s.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq) # 그룹에 가입

# from socket import *
# s = socket(AF_INET, SOCK_DGRAM)
# s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 4) # 멀티캐스트 TTL 설정
# s.sendto('Multicasting OK!!!'.encode('utf-8'), ('235.5.5.5', 9000))

from ftplib import FTP
print('---- connecting...')
ftp = FTP()
ftp.connect('127.0.0.1', 2121)
print('---- logging in...')
ftp.login()
print('---- getting list')
ftp.retrlines('LIST')
print('---- getting dir')
print(ftp.dir())
print('---- getting nlist')
print(ftp.nlst())

