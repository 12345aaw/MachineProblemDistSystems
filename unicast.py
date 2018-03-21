from __future__ import print_function
import socket
import threading
import site 
import datetime
import random
<<<<<<< HEAD
=======
import time

# Opens the configuration file
# The config file lists each node's characteristics, each on a separate line
# The three characteristics right now are ID Number, IP Address, and Port Number

config_file = open("config","r")

# Initializations of global variables
RECEIVED = []
DESTINATIONS = []
MYID = -1
MYIP = ""
MYPORT = 0
MYSOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Number of nodes in config file
# -3 to account for first min-max line, and two trailing whitespace lines

NUMOFNODES = sum(1 for line in open('config')) - 3
>>>>>>> 1a05782347084f211dfd9b71a77c1638ef84edfc


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
<<<<<<< HEAD
    sock.sendto(message, (IP,PORT))
    print("Sent \"", msg, "\" to process ", ID, ", system time is ", datetime.datetime.now().time(), sep='')
=======
    sock.sendto(myidandmessage, (ip,port))
    print("Sent \"", message, "\" to process ", id, ", system time is ", datetime.datetime.now().time(), sep='')

def channel_delay(destination,message):
    time.sleep(4)   # Delay for 4 seconds
    unicast_send(destination,message)

# Take min and max delay from config file

minmaxdelay = config_file.readline().rstrip('\n')
minandmax = minmaxdelay.split(" ")
min = float(minandmax[0])
max = float(minandmax[1])

for a in range(NUMOFNODES):



    # Read in the ID, IP, and PORT from the config file for each of the four connections

    line = config_file.readline().rstrip('\n')

    # Split line into ID, IP, PORT

    linearray = line.split(" ")
    ID = int(linearray[0])
    IP = linearray[1]
    PORT = int(linearray[2])

    # Decides which node this process will be

    if MYID == -1:
        MYID = int(raw_input("Type in your node ID number (0-3)"))

    # Creates sockets between all pairs of nodes and
    # appends nodes to a list as a tuple of ID, IP, PORT
    # and SOCK

    if a != MYID:
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    else:
        MYIP = IP
        MYPORT = PORT
        SOCK = MYSOCKET

    DESTINATIONS.append((ID,IP,PORT,SOCK))

# Bind socket to the process

MYSOCKET.bind((
    MYIP, # IP of processNumber 
    MYPORT)) # Port of processNumber
>>>>>>> 1a05782347084f211dfd9b71a77c1638ef84edfc




