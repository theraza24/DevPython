#Write a python program to get the IP Address

# Socket programming is a way of connecting two nodes on a network to communicate with each other. 

import socket  

hostname = socket.gethostname () 

print (hostname)

IP =  socket.gethostbyname (hostname)

print(IP)