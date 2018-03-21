from __future__ import print_function
import socket
import threading
import site 
import datetime
import random


# Unicast delivery (instructions want it to be called receive)
# Checks list for 'message' from 'source. If it contains the message, it is delievered
# and removed from the list
# Adds uniform random, simulated network delay time. 
# Min & max multiplied by 1000 for microseconds ---> milliseconds

def unicast_receive(selfnode, source, message):
    #if selfnode.RECEIVED.__contains__((source.MYID,message)):   
    time = (datetime.datetime.now() + datetime.timedelta(microseconds=random.uniform(source.MIN*1000,source.MAX*1000))).time()
    print("Received \"", message, "\" from process ", source.MYID, ", system time is ", time, sep='')

# Unicast receive
# Loops and listens for receptions to be put on list
# ends loop if 'close' is typed in

#def receive(selfnode):
#    sock = selfnode.MYSOCKET
#    while 1:
#        data = selfnode.MYSOCKET.recv(1024)
#        datasplit = data.split(" ")
#        id = int(datasplit[0])
#        data = datasplit[1]
#        selfnode.RECEIVED.append((id,data))
#        unicast_receive(selfnode,data)
#        if data == "close": break

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
    if(len(messagesplit)==2):
        msgid = messagesplit[0]
        msg = messagesplit[1]
    #message = "u " + message
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message, (IP,PORT))
    print("Sent \"", msg, "\" to process ", ID, ", system time is ", datetime.datetime.now().time(), sep='')




