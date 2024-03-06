#script utilisant une socket brute pour sniffer les paquets

import socket

# créer le socket raw
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

# lier le socket à l'interface publique
ip_host=("192.168.70.134",0)
sniffer.bind(ip_host)

# nous voulons les en-têtes IP inclus dans le paquet capturé
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

#activer le mode promiscuous
sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# lecture des paquets

while True:
    # lire un paquet
    raw_buffer = sniffer.recvfrom(65565)
    # analyse des en-têtes IP
    ip_header = raw_buffer[0][0:20]
    # affichage ip src et ip dst
    print("IP : ", ip_header[12:16], " -> ", ip_header[16:20])
    # affichage du type de protocole
    print("Protocol : ", ip_header[9])