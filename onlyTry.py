import socket, ssl, time, thread

host = "0.0.0.0"
port = 10023
socket_addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(socket_addr)
sock.listen(5)


print 'wait connected'
while 1:
    conn, client_addr = sock.accept()
    connstream = ssl.wrap_socket(conn, "mykeyfile.pem", "mycertfile.pem", server_side=True, ssl_version=ssl.PROTOCOL_TLSv1)
    print type(connstream)
    while 1:
        data = connstream.recv(1024)
        print "connected by",client_addr
        print "Message:", data

        print type(data)
        connstream.send("get it")

connstream.shutdown(socket.SHUT_RDWR)
connstream.close()