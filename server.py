import socket
import time

ip = '0.0.0.0'
port = 5000

addr = (ip, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(addr)
server_socket.listen(100)


client_socket, client_addr = server_socket.accept()     #socket.accept() return (conn, addr)
print('accepted')

while True:
    message = client_socket.recv(100).decode()
    if message == 'exit':
        server_socket.close()
        print('server closed')
        break
    print(">>>[{}] message : {}".format(client_addr, message))
    client_socket.sendall('Hi'.encode('utf-8'))