import receive as rc 
import send as se
import socket
import threading
import site 

# Opens the configuration file
# The config file lists each node's characteristics, each on a separate line
# The three characteristics right now are ID Number, IP Address, and Port Number

config_file = open("config","r")

# Initializations of global variables
DESTINATIONS = []
MYID = -1
MYIP = ""
MYPORT = 0
MYSOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Number of lines in config file divided by 3 for number of nodes
NUMOFNODES = sum(1 for line in open('config'))/3

for a in range(NUMOFNODES):

    # Read in the ID, IP, and PORT from the config file for each of the four connections

    line = config_file.readline()

    # Strips the new line character from the config file 

    ID = int(line.rstrip('\n'))
    
    line = config_file.readline()
    IP = line.rstrip('\n')
    line = config_file.readline()
    PORT = int(line.rstrip('\n'))

    # Need a socket for each node pair

    if MYID == -1:
        MYID = int(raw_input("Type in your process number (0-3)"))


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

threading.Thread(target=rc.unicast_receive, args = (DESTINATIONS[MYID][3],)).start()


while 1:
    decide = raw_input("What do you want to do?\n")
    if(decide[0:4] == "send"):
        sendTo = int(decide[5])
        sendString = decide[7:]
        se.unicast_send(DESTINATIONS[sendTo], sendString)
    if(decide[0:5] == "close"):
        se.unicast_send(DESTINATIONS[MYID], "close")
        break
