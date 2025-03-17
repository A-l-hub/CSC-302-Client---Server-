# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 09:39:08 2025

@author: akoro
"""
# client.py
import socket

def start_client():
    host = '127.0.0.1'  # Server address
    port = 12345        # Server port
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = "Hello from the client!"
    client_socket.send(message.encode())
    
    response = client_socket.recv(1024).decode()
    print(f"Server says: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()

