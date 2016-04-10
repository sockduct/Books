import socket
import ssl
import pprint
import time

# Constants
TIMEOUT = 3

# Without SSL
#sock = socket.socket()
# With SSL
context = ssl.create_default_context()
sock = context.wrap_socket(socket.socket(socket.AF_INET),
        server_hostname="www.googleapis.com")

# Old (v2?)
#sock.connect(('maps.google.com', 80))
sock.connect(('maps.googleapis.com', 443))
cert = sock.getpeercert()
print 'SSL Certificate Presented:'
pprint.pprint(cert)
print ''
# Old (v2?)
#sock.sendall(
#    'GET /maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'
#    '&output=json&oe=utf8&sensor=false HTTP/1.1\r\n'
#    'Host: maps.google.com:80\r\n'
#    'User-Agent: search4.py\r\n'
#    'Connection: close\r\n'
#    '\r\n')
sock.sendall(
    b'GET /maps/api/geocode/json?address=207+N.+Defiance+St%2C+Archbold%2C+OH'
    b'&key=AIzaSyDhMDnzWJqQAPNCn_jq_mTRBYPiMgIHKRI HTTP/1.1\r\n'
    b'Host: maps.googleapis.com\r\n'
    b'Connection: close\r\n'
    b'\r\n')

# Handle receiving data
# This doesn't work (making socket non-blocking) - may not be supported within SSL
# Make socket non-blocking
#sock.setblocking(0)
# Data storage
total_data = []
data = ''
begin = time.time()
while True:
    #if you got some data, then break after timeout
    if total_data and time.time() - begin > TIMEOUT:
        break
    #if you got no data at all, wait a little longer, twice the timeout
    elif time.time() - begin > TIMEOUT * 2:
        break
         
    data = sock.recv(8192)
    if data:
        total_data.append(data)
        #change the beginning time for measurement
        begin=time.time()
    else:
        #sleep for sometime to indicate a gap
        time.sleep(0.1)
     
#join all parts to make final string
rawreply = ''.join(total_data)
 
# This doesn't work, truncates the data
#rawreply = sock.recv(8192)
print 'Query Response:\n' + str(rawreply)

