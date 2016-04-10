##############################################################################
#
# Example UDP Client
#
##############################################################################

import socket
import sys

srvhost = '127.0.0.1'
srvport = 5555

try:
    clisock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

while True:
    clidata = raw_input('Message to send:  ')
    try:
        clisock.sendto(clidata,(srvhost,srvport))
        # Receive data from server (srvdata, srvaddr)
        srvconn = clisock.recvfrom(1024)
        srvdata = srvconn[0]
        srvaddr = srvconn[1]
        print 'Message from server [' + srvhost + ":" + str(srvport) + "] - " + srvdata
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

