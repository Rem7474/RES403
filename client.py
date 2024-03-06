#script client utilisant la librairie socket pour communiquer avec le serveur sur le port 2000
import socket

# Création d'un objet socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
IP="192.168.70.134"
clientsocket.connect((IP, 2000))

# Envoi de données
clientsocket.send(b'Hello, world')