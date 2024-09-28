import socket 

sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient.connect(("localhost",8005))
print("Server said: ",sClient.recv(256).decode("utf-8"))
msg1 = input("Unesite jedan broj od jedan do pet")
sClient.send(bytes(msg1, "utf-8"))
msg2 = input("Unesite drugi broj: ")
sClient.send(bytes(msg2,"utf-8"))
print("Result is: ",sClient.recv(256).decode("utf-8"))
sClient.close()
