from __future__ import print_function
import socket
import threading
import site 
import datetime
import random


# Unicast delivery (instructions want it to be called receive)
# Adds uniform random, simulated network delay time. 
# Min & max multiplied by 1000 for microseconds ---> milliseconds

def unicast_receive(selfnode, source, message):
    time = datetime.datetime.now()
    print("Received \"", message, "\" from process ", source.MYID, ", system time is ", time, sep='')


# Unicast send
# sends a message with sender's ID to the destination node
# destination is a tuple of ID Number, IP Address, Port Number
# and Socket Object of the destination.

def unicast_send(destination,message):
    ID = destination.MYID
    IP = destination.MYIP
    PORT = destination.MYPORT
    msg = message
    messagesplit = message.split(" ")
    if(len(messagesplit)>=2):
        msgid = messagesplit[0]
        msg = messagesplit[1]
    #message = "u " + message
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (IP,PORT))
    print("Sent \"", msg, "\" to process ", ID, ", system time is ", datetime.datetime.now().time(), sep='')




