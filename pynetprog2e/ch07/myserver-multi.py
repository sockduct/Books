#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - server_simple.py
# Simple server that only serves one client at a time; others have to wait.
#
# For multiple Processes - does not work in Python 2.x on Windows, see:
# https://bugs.python.org/issue5879
# Could work in Python 3.x on Windows but Python changes string processing and
# program needs to be fixed to accomodate this.  Right now get:
# TypeError: Can't convert 'bytes' object to str implicitly
#
# For multiple threads works
#

import random
import socket
import sys
import time
from multiprocessing import Process
from threading import Thread

PORT = 1060
qa = (('What is your name?', 'My name is Sir Lancelot of Camelot.'),
      ('What is your quest?', 'To seek the Holy Grail.'),
      ('What is your favorite color?', 'Blue.'))
qadict = dict(qa)
randans = ("I'm not sure.","That's a lame question.",
            "I don't understand what you're asking.","You're crazy.",
            "Go away.","Your mother is a hamster.")
WORKER_CLASSES = {'thread': Thread, 'process': Process}
WORKER_MAX = 10
CONN_MAX = 10

def recv_until(sock, suffix):
    message = ''
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise EOFError('socket closed before we saw %r' % suffix)
        message += data
    return message

def setup():
    if len(sys.argv) != 2:
        #print >>sys.stderr, 'usage: %s interface' % sys.argv[0]
        print('usage: %s interface' % sys.argv[0])
        exit(2)
    interface = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, PORT))
    sock.listen(CONN_MAX)
    print('Ready and listening at %r port %d' % (interface, PORT))
    return sock

def handle_client(client_sock):
    try:
        while True:
            question = recv_until(client_sock, '?')
            if question in qadict:
                answer = qadict[question]
            else:
                raindex = random.randint(0,len(randans)-1)
                answer = randans[raindex]
            client_sock.sendall(answer)
    except EOFError:
        client_sock.close()

def server_loop(listen_sock):
    workers = []
    while True:
        client_sock, sockname = listen_sock.accept()
        worker = Worker(target=handle_client, args=(client_sock,))
        #worker.daemon = True
        workers.append(worker)
        worker.start()
        #handle_client(client_sock)

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[2] not in WORKER_CLASSES:
        #print >>sys.stderr, 'usage: server_multi.py interface thread|process'
        print('usage: server_multi.py interface thread|process')
        sys.exit(2)
    Worker = WORKER_CLASSES[sys.argv.pop()]  # setup() wants len(argv)==2
    #
    listen_sock = setup()
    server_loop(listen_sock)

