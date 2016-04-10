##############################################################################
#
# Example UDP Server
#
##############################################################################

import socket
import sys

srvhost = ''  # Listen on all available interfaces
srvport = 5555  # Port to listen on

# From example, perhaps a bit much?
try:
    srvsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error, msg:
    print 'Failed to create socket. Error Code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# Bind socket to local host and port
try:
    srvsock.bind((srvhost,srvport))
except socket.error, msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

# Process client connections
if srvhost == '':
    srvname = '*'
else:
    srvname = srvhost
print "Listening on [" + srvname + ":" + str(srvport) + "] - Ready:"
while True:
    cliconn = srvsock.recvfrom(1024)
    clidata = cliconn[0]
    cliaddr = cliconn[1]
    if not clidata:
        break
    myreply = 'OK...' + clidata
    srvsock.sendto(myreply,cliaddr)
    print 'Message from [' + cliaddr[0] + ':' + str(cliaddr[1]) + '] - ' + clidata.strip()

srvsock.close()

