import socket                                         
import online_chat as oc

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
port = 9999                                          

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           
msg='1'
# establish a connection
msg1 = '11'

#starting the connection
clientsocket,addr = serversocket.accept()
print("Got a connection from %s" % str(addr)) 

#decoding the first message
clientsocket.send(msg1.encode('utf-8')) 
ms1=clientsocket.recv(2048)
msg=ms1.decode('utf-8')

#initialzing the chatbot
bot=oc.chatbot(int(msg))


while msg!='0010':
 ms1=clientsocket.recv(8192)
 msg=ms1.decode('utf-8')
 print('Client: '+msg)
 if msg =='00':
  print('disconnecting')
 else:
  msg1=bot.reply(msg)[0]
  clientsocket.send(msg1.encode('utf-8'))

clientsocket.close()   
serversocket.close()

