from __future__ import print_function
import socket
import threading
import site 
import datetime
import random



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


# Unicast delivery (instructions want it to be called receive)
# Checks list for 'message' from 'source. If it contains the message, it is delievered
# and removed form the list

def unicast_receive(source, message):
    if RECEIVED.__contains__((source,message)):
        RECEIVED.remove((source,message))
        time = (datetime.datetime.now() + datetime.timedelta(seconds=random.uniform(min,max))).time()
        print("Received ", message, " from process ", source, ", system time is ", time, sep='')

# Unicast receive
# Loops and listens for receptions to be put on list
# ends loop if 'close' is typed in

def receive(id, socket, received):
    sock = socket
    while 1:
        data = sock.recv(1024)
        datasplit = data.split(" ")
        id = datasplit[0]
        data = datasplit[1]
        received.append((id,data))
        unicast_receive(id,data)
        if data == "close": break

# Unicast send
# sends a message with sender's ID to the destination node
# destination is a tuple of ID Number, IP Address, Port Number
# and Socket Object of the destination.

def unicast_send(destination,message):
    id = destination[0]
    ip = destination[1]
    port = destination[2]
    myidandmessage = str(MYID) + " " + message

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(myidandmessage, (ip,port))
    print("Sent \"", message, "\" to process ", id, ", system time is ", datetime.datetime.now().time(), sep='')

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

# Separate thread for receiving and listening for unicasts

threading.Thread(target=receive, args = (DESTINATIONS[MYID][0],DESTINATIONS[MYID][3],RECEIVED)).start()

# Send messages to other nodes using the format:
# send (# of node) (message)
# type in 'close' to exit to terminal

while 1:
    decide = raw_input("What do you want to do?\n")
    if(decide[0:4] == "send"):
        sendTo = int(decide[5])
        sendString = decide[7:]
        unicast_send(DESTINATIONS[sendTo], sendString)
    if(decide[0:5] == "close"):
        unicast_send(DESTINATIONS[MYID], "close")
        break
