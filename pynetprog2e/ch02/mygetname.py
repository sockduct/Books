import socket

#hostname = 'maps.google.com'
hostname = 'yahoo.com'

# IPv4-only
#addr = socket.gethostbyname(hostname)
# AF Neutral (IPv4/IPv6)
# Note - IPv6 only works if a global address is present on the host
print 'Resolving ' + hostname + '...'
addr = socket.getaddrinfo(hostname,None)

# gethostbyname only returns a single address
#print 'The address of', hostname, 'is', addr
print 'Results:'
for elmt in addr:
    print elmt

