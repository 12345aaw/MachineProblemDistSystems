from __future__ import print_function
import socket
import datetime
import random

# Receives a message from sock and prints the message out

def unicast_receive(id, socket):
    sock = socket
    ID = id
    kill = False
    while not kill:
        data = sock.recv(1024)
        if data == "close": break
        time = (datetime.datetime.now() + datetime.timedelta(seconds=random.uniform(0.5,1.0))).time()
        print("Received ", data, " from process ", id, ", system time is ", time, sep='')
