import socket 

sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient.connect(("localhost",8005))
print("Server said: ",sClient.recv(256).decode("utf-8"))
msg = input("Unesite jedan broj od 1 do 5 ")
sClient.send(bytes(msg,"utf-8"))
print("Server said: ",sClient.recv(256).decode("utf-8"))
sClient.close()
