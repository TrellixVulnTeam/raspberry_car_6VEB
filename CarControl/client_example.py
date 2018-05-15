import socket
import pygame

s = socket.socket()
s.connect(('localhost', 1090))
s.send(b'00/1500/90')
s.close()
