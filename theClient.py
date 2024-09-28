import socket 


sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sClient.connect(("localhost",8005))
prvaPorukaSaServera = sClient.recv(256).decode("utf-8")
print(prvaPorukaSaServera)
brojRedova = input("Molimo unesite broj redova: ").strip()
brojKolona = input("Molimo unesite broj kolona: ").strip()
sClient.send(bytes(brojRedova,"utf-8"))
sClient.send(bytes(brojKolona,"utf-8"))

sClient.close()