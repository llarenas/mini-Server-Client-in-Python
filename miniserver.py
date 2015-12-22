'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

#!/usr/bin/python

import socket
import sys

#create a tcp/ip socket t listen on
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#prevent from "address already in use" upn server restart
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to port 8081 n all intefaces
server_address = ('localhost', 8081)
print ('starting up on %s port %s') % server_address
server.bind(server_address)

#listen for connections
server.listen(5)

#wait for incoming connections
connection, client_address = server.accept()
print ('connection from ', connection.getpeername())

#lets receive something
data = connection.recv(4096)
if data:
    print ("Received ", repr(data))

    #send it back nicely formatted
    data = data.rstrip()
    connectin.send("%S\n%s\n%S\n" % ('-'*80, data.center(80), '-' *80))
    print("Response sent!")

#close the connection from our side
connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
connection.close()
print ("Connection closed.")

#aaaand stop listening
server.close()
    


