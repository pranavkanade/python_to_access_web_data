import socket

mysok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysok.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysok.send(cmd)


while True:
    data = mysok.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysok.close()

# GET http://www.dr-chuck.com/page1.htm HTTP/1.0