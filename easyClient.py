import socket, ssl, time

host = "192.168.1.109"
port = 10023
socket_addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(sock, ca_certs="mycertfile.pem", cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(socket_addr)

while 1:
    sendDATA = raw_input("input:")
    if sendDATA == 'quit':
        ssl_sock.close()
        break
    else:
        ssl_sock.send(sendDATA)
        getData = ssl_sock.recv(1024)
        print "Message:", getData