import socket
import random

s = socket.socket()
dict_q = {}
l = []
for i in range(1 , 101):
    l.append(i)

ans = []
for i in range(1 , 101):
    ans.append(3 * i)

dict_q = {k:v for (k, v) in zip(l , ans)}
s.bind(('' , 12345))
#print(dict_q)
s.listen(5)
print("Server is listening")
try:
    while True:
        c , addr = s.accept()
        #print("got connection from " , addr)
        var = str(l[random.randint(0 , len(l))])

        c.send("What is 3 multiplied by " + var)
        
        t = int(c.recv(1024))
        if(t==dict_q[int(var)] and t!=0):
            c.send("Correct")
        else:
            c.send("Wrong")
        dict_q.pop(int(var))
        l.remove(int(var))
        c.close()
except KeyboardInterrupt:
    c.close()
    s.shutdown(socket.SHUT_RDWR)
