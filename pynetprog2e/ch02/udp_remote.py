#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_remote.py
# UDP client and server for talking over the network

import random, socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Maximum size of a UDP datagram
MAX = 65535
# Arbitrary server port
PORT = 1060

if 2 <= len(sys.argv) <= 3 and sys.argv[1] == 'server':
    interface = sys.argv[2] if len(sys.argv) > 2 else ''
    s.bind((interface, PORT))
    print 'Listening at', s.getsockname()
    while True:
        data, address = s.recvfrom(MAX)
        if random.randint(0, 1):
            print 'The client at', address, 'says:', repr(data)
            s.sendto('Your data was %d bytes' % len(data), address)
        else:
            print 'Pretending to drop packet from', address

elif len(sys.argv) == 3 and sys.argv[1] == 'client':
    hostname = sys.argv[2]
##### Rather than specifying the destination address with sendto,
##### use connect to specify the destination address/port
##### Note - in Windows, if there is nothing listening here locally
##### an error will be raised
    s.connect((hostname, PORT))
##### Another benefit of connect, is that after doing it and then
##### doing a recv, the socket will only accept data with an
##### address/port which matches what was set in connect; Whereas
##### with just sendto, the socket will accept from any address
##### and port (susceptible to spoofing)
    # Can only do on Windows if do connect/bind/sendto first
    print 'Client socket name is', s.getsockname()
    delay = 0.1
    while True:
######### Note - in Windows, if send to a local interface address or
######### the loopback and there isn't a server listening, an error
######### will be raised (assuming this is O/S but could be McAfee
######### endpoint security too)
        s.send('This is another message')
        # Alternative to connect & send
        ##s.sendto('This is another message',(hostname,PORT))
        print 'Waiting up to', delay, 'seconds for a reply'
######### Set a timeout on trying to read data (blocking)
######### After timeout expires, a socket.timeout error will be thrown
        s.settimeout(delay)
        try:
            data = s.recv(MAX)
        except socket.timeout:
######### Catch the socket.timeout error and handle it
######### When retrying a send, use exponential backoff so as not to
######### cause/worsen congestion or a needless backlog
            delay *= 2  # wait even longer for the next request
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
        else:
            break   # we are done, and can stop looping
            
    print 'The server says', repr(data)

else:
    print >>sys.stderr, 'usage: udp_remote.py server [ <interface> ]'
    print >>sys.stderr, '   or: udp_remote.py client <host>'
    sys.exit(2)

