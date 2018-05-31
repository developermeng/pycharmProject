import time,datetime,struct,MySQLdb
timestr = "".join(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print timestr

with open('time.txt','a+') as f:
    f.write(timestr + '\n')

with open('profinet-wireshark-bug.pcap','rb+') as f:
    result = f.read(16)
    data = struct.unpack('16b', result)
    print(data)
