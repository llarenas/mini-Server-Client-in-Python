'''
Written By Ronel B. Llarenas
Github.com/llarenas
'''

#!/usr/bin/python
# Mini ckient prgram
# make sure nga ang misiserver.py is running

import socket
s = socket.socket(socket.AF_INET, socket.SOCK__STREAM)
s.connect(('localhost', 8081))
s.send('Happy Hacking')
data = s.recv(1024) #1024 bytes
s.close()
print ('Received: ')
print (data)
