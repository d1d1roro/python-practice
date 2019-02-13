# import getpass
# import sys
# import telnetlib

# host = "192.168.0.10" 
# user = input("Enter Username:")
# password = getpass.getpass()
# tn = telnetlib.Telnet(host)
# tn.read_until(b"Username:")
# tn.write(user.encode("ascii")+ b"\n")

# if password:
#     tn.read_until(b"Password:") 
#     tn.write(password.encode("ascii")+b"\n")

# tn.write(b"dir \n")
# tn.write(b"cisco\n")
# tn.write(b"conf t\n")
# tn.write(b"int loopback 1\n")
# tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
# tn.write(b"end\n")
# tn.write(b"exit\n")
# print(tn.read_all().decode("ascii"))