import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]
n = 10;
i=0;
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while i<n :
 print ("Enter data to transmit: ENTER to quit")
 data= random.randint(0,1000)
# print(data)
 i=i+1
# if not len(data):
#	 break
#    s.sendall(data.encode('utf-8'))
 s.sendto(str(data), server_address)

#s.shutdown(1)
