import socket

addr = ('0.0.0.0', 8899)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind(addr)
mysock.listen(5)

while 1:
    client_conn, client_addr = mysock.accept()
    while 1:
        try:
            data = client_conn.recv(1024)
            print type(client_addr)
            print type(data)
            print client_addr
            print data
            client_conn.sendall('Get message')
        except:
            break

client_conn.close()