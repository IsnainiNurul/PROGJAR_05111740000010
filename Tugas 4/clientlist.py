import socket
import sys
from time import sleep
import base64
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8889)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
pesan = (b"list")
sock.send(pesan)
print("Request terkirim")
data = sock.recv(1024)
print("List isi file : \n"+data.decode())
sock.close()
