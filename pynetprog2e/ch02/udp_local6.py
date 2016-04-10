#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_local.py
# UDP client and server on localhost

import socket, sys
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

# Maximum size of a UDP datagram
MAX = 65535
# Arbitrary server port
PORT = 1060

if sys.argv[1:] == ['server']:
    s.bind(('::1', PORT))
    print 'Listening at', s.getsockname()
    while True:
        data, address = s.recvfrom(MAX)
        print 'The client at', address, 'says', repr(data)
        s.sendto('Your data was %d bytes' % len(data), address)

elif sys.argv[1:] == ['client']:
    # In Windows at least, this will result in an error before binding
    # or sending data
    #print 'Address before sending:', s.getsockname()
##### Note - client can just send arbitrary messages without binding/connecting
    s.sendto('This is my message', ('::1', PORT))
    print 'Address after sending', s.getsockname()
    data, address = s.recvfrom(MAX)  # overly promiscuous - see Chapter 2
    print 'The server', address, 'says', repr(data)

else:
    print >>sys.stderr, 'usage: udp_local.py server|client'
