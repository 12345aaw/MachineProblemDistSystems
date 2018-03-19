from __future__ import print_function
import socket
import datetime
import random

# Receives a message from sock and prints the message out

def unicast_receive(id, socket, min, max):
    sock = socket
    ID = id
    kill = False
    while not kill:
        data = sock.recv(1024)
        if data == "close": break
        time = (datetime.datetime.now() + datetime.timedelta(seconds=random.uniform(min,max))).time()
        print("Received ", data, " from process ", ID, ", system time is ", time, sep='')
