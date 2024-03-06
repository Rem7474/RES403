#script client utilisant la librairie socket pour communiquer avec le serveur sur le port 2000
import socket

# Création d'un objet socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tupple contenant l'adresse IP et le port du serveur
server=("192.168.70.134",2000)
clientsocket.connect(server)

# Variable contenant les données a envoyer
data = "Bonjour, serveur !"
# Envoi de données
clientsocket.send(data.encode())

# Réception de données
data = clientsocket.recv(1024)
# Affichage des données reçues
print(data.decode())

# Fermeture de la connexion
clientsocket.close()