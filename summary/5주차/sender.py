from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 4) # 멀티캐스트 TTL 설정
s.sendto('Multicasting OK!!!'.encode('utf-8'), ('235.5.5.5', 9000))