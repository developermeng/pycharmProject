import socket

#get local ip
def getLocalIP():
    tempSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tempSock.connect(('8.8.8.8', 80))
    local_ip = tempSock.getsockname()[0]
    return local_ip

if __name__ == "__main__":
    print getLocalIP()
