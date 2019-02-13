from socket import *
import struct

# 그룹에 가입하기
def strip2binip(ip):
    def inet_addr(ip):
        "convert decimal dotted quad string to long integer"
        return struct.unpack('>L', inet_aton(ip))[0]
    return struct.pack('ll', htonl(inet_addr(ip)), INADDR_ANY)

# 소켓 설정
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', 9000))

# 그룹에 가입하기
mreq = strip2binip('235.5.5.5') # 그룹 주소
s.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

print('데이터를 받습니다.')
msg, addr = s.recvfrom(1024)
print('[보낸 주소](%s, %s)' % addr)
print('[받은 데이터]%s' % msg)

# 그룹에서 탈퇴하기
s.setsockopt(IPPROTO_IP, IP_DROP_MEMBERSHIP, mreq)
s.close()