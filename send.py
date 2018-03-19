import socket

# sends a message to the destination node
# destination is a tuple of ID Number, IP Address, Port Number
# and Socket Object of the destination.

def unicast_send(destination,message):
    IP = destination[1]
    PORT = destination[2]
    MESSAGE = message

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (IP,PORT))
