# !/usr/bin/env python

# import socket
# import time

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOST = "34.107.124.213"
# PORT = 31030

# s.connect((HOST,PORT))

# rep1 = s.recv(4096).decode('utf-8')
# s.recv(1024)
# print "-------------------------------------" 
# print rep1
# num1 = int(rep1.split("<<")[1].split(">>")[0])
# print str(num1) 
# res1 = hex(num1)
# print str(res1) 

# s.sendall(str(res1))


# rep2 = s.recv(4096)
# print "-------------------------------------"
# print rep2
# # num1 = int(rep1.split("<<")[1].split(">>")[0])
# # print(str(num1))
# # res1 = hex(num1)
# # print("0x"+str(res1).split('x')[1])
# # time.sleep(5)
# # s.send(str(res1))

# s.close()
import pwn 

HOST = "34.107.124.213"
PORT = 31030

s = pwn.remote(HOST,PORT)


rep1 = s.recv()
# s.recv()
print "-------------------------------------" 
print rep1
ans1 = int(rep1.split("<<")[1].split(">>")[0])
print str(ans1) 
res1 = str(hex(ans1))
print res1
s.sendline(res1)

rep2 = s.recv()
print "-------------------------------------" 
print rep2
ans2 = rep2.split("<<")[1].split(">>")[0]
print ans2 
res2 = ans2.decode("hex")
print res2
s.sendline(res2)

rep3 = s.recv()
print "-------------------------------------" 
print rep3
ans3 = rep3.split("<<")[1].split(">>")[0]
print ans3 
res3 = "".join([chr(int(x,8)) for x in ans3.split(' ')])
print res3
s.sendline(res3)

flag = s.recv()
print "-------------------------------------" 
print "FLAG:                                " 
print "-------------------------------------" 
print flag

s.close()