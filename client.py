import socket

server_ip = '0.0.0.0'
server_port = 5000

server_addr = (server_ip, server_port)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(server_addr)

while True:
    client_message = input('>>>')
    socket.sendall(client_message.encode(encoding='utf-8'))
    if client_message == 'exit':
        socket.close()
        print('closed')
        break
    data = socket.recv(100)
    message = data.decode()
    print('echo message: ', message)


