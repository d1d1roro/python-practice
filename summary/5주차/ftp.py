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