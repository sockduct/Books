#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - client.py
# Simple Lancelot client that asks three questions then disconnects.

import socket, sys, time, lancelot

def client(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(lancelot.qa[0][0])
    answer1 = lancelot.recv_until(s, '.')  # answers end with '.'
    print answer1
    time.sleep(2)
    s.sendall(lancelot.qa[1][0])
    answer2 = lancelot.recv_until(s, '.')
    print answer2
    time.sleep(2)
    s.sendall(lancelot.qa[2][0])
    answer3 = lancelot.recv_until(s, '.')
    print answer3
    time.sleep(2)
    s.close()

if __name__ == '__main__':
    if not 2 <= len(sys.argv) <= 3:
        print >>sys.stderr, 'usage: client.py hostname [port]'
        sys.exit(2)
    port = int(sys.argv[2]) if len(sys.argv) > 2 else lancelot.PORT
    client(sys.argv[1], port)
