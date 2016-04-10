import socket
import string

# Setup Server Socket
srvport = 4444
srvsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srvsock.bind(('',srvport))
srvsock.listen(1)
clisock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliconn = ()
cliaddr = ''
cliport = 0

# Take Input
print "Listening on *:" + str(srvport) + " - Ready:"
while True:
    (clisock,cliaddr) = srvsock.accept()
    #clisock.addr = srvsock.accept()
    cliaddr,cliport = cliaddr
    block = clisock.recv(65535)
    clisock.close()
    print "\nInbound connection from " + cliaddr + ":" + str(cliport) + " - Received:\n" + block + "\n"

