# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# #connecting
# s.connect(("localhost", 63303))
#
# message = "Hello"
# s.send(message.encode())
#
# data = s.recv(32)
# print(data.decode())
#
# #Connection Closed
# s.close()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 63300))
name = input("Enter file name: ")
path = input("Enter file path: ")

s.send(name.encode())
message = s.recv(1024)
print(message.decode())
if message.decode() == "404NotFound":
    s.close()
else:
    data = s.recv(1024)
    f = open(path, 'w')
    f.write(data.decode())
    f.close()
    s.close()

