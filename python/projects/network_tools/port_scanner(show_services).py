#!/usr/bin/env python3

import socket

Ports = [21,22,25,3306,4320]

for i in range (0,5):
    s = socket.socket()
    Port = Ports[i]


s.connect(('192.168.0.247', Port))

answer = s.recv (1024)

print('PORT:', Port, 'SERVICE:', answer)

s.close()
