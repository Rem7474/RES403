#script serveur utilisant le module socket pour récupérer les données du client depuis le port 2000
import socket

# Création d'un objet socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtenir l'ip de la machine
ip = "192.168.70.134"
port = 2000

# Lier à l'adresse et au port
serversocket.bind((ip, port))

# Nombre maximum de connexions en attente
serversocket.listen(1)

while True:
    # Établir une connexion
    clientsocket,addr = serversocket.accept()
    print(f"Connexion depuis {addr[0]}:{addr[1]}")
    msg = 'Connexion réussie : message bien reçu !' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()