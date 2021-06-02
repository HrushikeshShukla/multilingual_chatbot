#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
ms = s.recv(2048) 
msg=ms.decode('utf-8')
if msg== '11':
 print('connected')     

##selecting the language
print("***Welcome to multilinugal chatbot.***")
print("***बहुभाषिक ​​चॅटबॉटमध्ये आपले स्वागत आहे.***")
print("\n \nPlease Select language:\nकृपया भाषा निवडा:")
indx=int(input("\n मराठीसाठी 1 दाबा,Press 2 for english: "))
if indx==1:
    print("Starting marathi version.\n मराठी आवृत्ती सुरू करीत आहे.")
    msg1='1'
    s.send(msg1.encode("utf-8"))
    while msg1 != '0010':
        msg1=input('आपण :')
        if msg1=='00':
            print('disconnect initiated')
            s.send(msg1.encode("utf-8"))
            continue
        s.send(msg1.encode("utf-8"))
        ms=s.recv(8192)
        msg=ms.decode('utf-8')
        print('रोबोट :'+msg)

else: 
    print("Starting english version.")   
    msg1='2'
    s.send(msg1.encode("utf-8"))
    while msg1 != '0010':
        msg1=input('You :')
        if msg1=='00':
            print('disconnect initiated')
            s.send(msg1.encode("utf-8"))
            continue
        s.send(msg1.encode("utf-8"))
        ms=s.recv(8192)
        msg=ms.decode('utf-8')
        print('bot :'+msg)                            

s.close()
#Now run this server.py in the background and then run the above client.py to see the result.

