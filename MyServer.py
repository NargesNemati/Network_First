import socket
import os
import os.path
from os import path
import urllib.request
import urllib.request
from os import path


urllib.request.urlretrieve("http://www.python.org/", "ServerFile/www.python.org.html")
urllib.request.urlretrieve("https://www.wikipedia.org/", "ServerFile/www.wikipedia.org.html")
urllib.request.urlretrieve("https://stackoverflow.com/", "ServerFile/stackoverflow.com.html")
urllib.request.urlretrieve("https://www.uptvs.com/", "ServerFile/www.uptvs.com.html")
urllib.request.urlretrieve("https://soft98.ir/", "ServerFile/soft98.ir.html")
urllib.request.urlretrieve("https://www.yasdl.com/", "ServerFile/www.yasdl.com.html")
urllib.request.urlretrieve("https://upmusics.com/category/single-tracks/", "ServerFile/upmusics.com.html")
urllib.request.urlretrieve("https://www.w3schools.com/cs/index.php/", "ServerFile/www.w3schools.com.html")
urllib.request.urlretrieve("https://jdk.java.net/", "ServerFile/jdk.java.net.html")
urllib.request.urlretrieve("https://translate.google.com/", "ServerFile/translate.google.com.html")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 63300))
s.listen(1)
while True:
    print("Hi Im ready")
    connection, client = s.accept()
    message = connection.recv(1024)
    p = "ServerFile/"
    IsExist = ""
    pathFile = p + message.decode()
    if(path.exists(pathFile)):
        IsExist="200OK"
        connection.send(IsExist.encode())
        f = open(pathFile, 'r')
        lines = []
        while True:
            line = f.readline()
            if line == '':
               break
            lines.append(line)
        f.close()
        connection.send(line.encode())
        connection.close()
    else:
        IsExist="404 Not Found"
        connection.send(IsExist.encode())
        connection.close()
