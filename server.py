#script serveur utilisant le module socket pour récupérer les données du client depuis le port 2000
import socket

# Création d'un objet socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tupple avec l'adresse et le port de la machine
server = ("192.168.70.134", 2000)

# Lier à l'adresse et au port
serversocket.bind(server)

# Nombre maximum de connexions en attente
serversocket.listen(1)
print("Le serveur est prêt à recevoir des données")

# Accepter une connexion
clientsocket,client_address  = serversocket.accept()
print(f"Connexion depuis {client_address [0]}:{client_address [1]}")

# Récupérer les données du client
data = clientsocket.recv(1024)
print('Message reçu :', data.decode('utf-8'))

# Envoyer un message au client
msg = "Connexion réussie : message bien reçu !"
clientsocket.send(msg.encode('utf-8'))
clientsocket.close()