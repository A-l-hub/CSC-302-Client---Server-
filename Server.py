# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 09:40:15 2025

@author: akoro
"""

# server.py
import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port to listen on
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")
    
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    
    message = conn.recv(1024).decode()
    print(f"Client says: {message}")
    
    response = "Hello from the server!"
    conn.send(response.encode())
    
    conn.close()
    server_socket.close()
    print("Server shut down.")

if __name__ == "__main__":
    start_server()