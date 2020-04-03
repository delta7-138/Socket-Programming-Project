import socket
from threading import *
import time

# def send_info(button):
#     time.sleep(10000)
#     if(button!="0"):
#         return 
#     print "Too Slow"


try:
    while True:
        button = "0"
        c = socket.socket()
        c.connect(('127.0.0.1' , 12345))
        #c.settimeout(10)
        #print("Connected")
        print(c.recv(1024))
        # Thread(target = send_info , args = button).start()

        # button = raw_input("Press Enter if you have the answer")
        #time_obj = threading.Timer(10 , send_info)
        c.send(raw_input())
        print(c.recv(1024))
        c.close()
except KeyboardInterrupt:
    c.send("0")
    c.close()
    print("Connection closed")