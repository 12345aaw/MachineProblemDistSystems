import socket

# Receives a message from sock and prints the message out

def unicast_receive(socket):
    sock = socket
    kill = False
    while not kill:
        data = sock.recv(1024)
        if data == "close": break
        print "received message:", data
