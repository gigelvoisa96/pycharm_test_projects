import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect("", 80)
cmd = 'GET http://'