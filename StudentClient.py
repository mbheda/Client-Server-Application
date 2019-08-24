# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from socket import *
import sys
import math
import os

host = input('Enter the host name: ')
port = int(input('Enter the port name: '))
request = input('Enter the file name: ')
f_save = input('Enter the file name to save: ')

try:
  query = 'GET /'+ request + ' HTTP/1.0'

  client_socket = socket(AF_INET, SOCK_STREAM)

  client_socket.connect((host, port))

  client_socket.send(query)

  print('receiving data...')
  data = client_socket.recv(1024)

  fileData = ''
  print(data)
  data = data.split('\n')
  for i in data[2:]:
      fileData = fileData + i + '\n'
  f = open(f_save, 'wb')
  f.write(fileData)
  print('Successfully got the file')
  f.close()
  client_socket.close()

  print('connection closed')
  
except Exception as e:
    client_socket.close()