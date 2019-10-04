# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
i = 0

while (i < 10):

    x = {"name" : "John",
     "age": 30,
     "city": "New York"}
    data = json.dumps(x)
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
    print (data)
    i += 1

s.shutdown(1)


