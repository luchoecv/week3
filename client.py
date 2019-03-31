import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 1234))
    s.send(bytes("I'm the client","utf-8"))
    data = s.recv(1024)

print('Received', repr(data))