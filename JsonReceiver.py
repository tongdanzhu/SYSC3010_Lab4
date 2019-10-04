# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    buf = buf.decode('utf-8')
    y = json.loads(buf)
    print ("Received %s bytes from %s %s: " % (len(buf), address, y))

s.shutdown(1)
