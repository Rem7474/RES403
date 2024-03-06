#script utilisant une socket brute pour sniffer les paquets

import socket

# le socket en mode promiscuous
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW)


# lire un paquet pour afficher ip src et ip dst + type de protocole

while True:
    print(sniffer.recvfrom(65565))
