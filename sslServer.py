import socket, ssl, time, thread

host = "0.0.0.0"
port = 10024
socket_addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(socket_addr)
sock.listen(5)

def sslDealer(mysock):
    client_conn, client_addr = mysock.accept()
    sslstream = ssl.wrap_socket(client_conn, "mykeyfile.pem", "mycertfile.pem", server_side=True, ssl_version=ssl.PROTOCOL_TLSv1)
    while 1:
        try:
            cmd = sslstream.recv(1024)
            print "ssl_client IP:", client_addr[0]
            print "ssl_client PORT:", client_addr[1]
            print "CMD:", cmd
            sslstream.send("Message geted: " + str(cmd))
        except:
            #break
            return sslstream

if __name__ == "__main__":
    while 1:
        try:
            connstream = sslDealer(sock)
        except:
            continue

    connstream.shutdown(socket.SHUT_RDWR)
    connstream.close()
