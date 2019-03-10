import socket
import getTemperature
from datetime import datetime
from time import sleep

s = socket.socket()

port = 5000
s.bind(('', port))

while True:
    print('listening')
    s.listen(5)
    c, addr = s.accept()
    print('receiving')
    print(c.recv(4096))
    while True:
        print('sending')
        #now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        temp = getTemperature.getTemperature()
        try:
            #c.send(now)
            c.send(temp)
            break
        except:
            break
        sleep(1)
    c.close()
s.close()

