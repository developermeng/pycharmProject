import socket, ssl, time

host = "127.0.0.1"
port = 8899
socket_addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(socket_addr)

while 1:
    sendDATA1 = raw_input("input data1:")
    sendDATA2 = raw_input("input_data2:")
    sendDATA = [sendDATA1, sendDATA2]
    sock.sendall(sendDATA)
    getData = sock.recv(1024)
    print "Message:", getData

sock.close()
