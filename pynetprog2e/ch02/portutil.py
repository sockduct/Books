# Imports
import argparse
import socket

# Main
parser = argparse.ArgumentParser(description='lookup port number by name or vice versa')
#
# Positional argument
parser.add_argument('portval',help='lookup the port number for a given service (or vice versa with -n)')
#
# Optional argument
parser.add_argument('-n','--number',help='lookup service name for a given port number',action='store_true')
#
# Parse arguments
args = parser.parse_args()
#
# Reverse lookup if --number (or -n) passed
if args.number:
    portsvc = socket.getservbyport(int(args.portval))
    print 'Result:  ' + str(portsvc)
else:
    # Note socket.getservbyname takes a servicename and an optional protocolname (tcp|udp)
    # In some cases, the service differs depending on if the protocol is TCP or UDP
    portnum = socket.getservbyname(args.portval)
    print 'Result:  ' + str(portnum)

