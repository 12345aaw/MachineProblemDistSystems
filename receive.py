from __future__ import print_function
import socket
import datetime
import random

# Receives a message from sock and queues it for delivery

def unicast_receive(id, socket, received):
    sock = socket
    ID = id
    while 1:
        data = sock.recv(1024)
        received.append((ID,data))
        if data == "close": break
        
        

