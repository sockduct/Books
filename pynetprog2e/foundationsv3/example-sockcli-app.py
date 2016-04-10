import socket
import string

srvhost = '127.0.0.1'
srvport = 4444
clisock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clisock.connect((srvhost,srvport))
print "Connected to " + str(srvhost) + ":" + str(srvport) + " - Ready:"
while True:
    userinput = raw_input()
    clisock.send(userinput)
    clisock.close
    print "\nSent:\n" + userinput + "\n"

