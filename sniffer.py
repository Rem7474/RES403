#script utilisant une socket brute pour sniffer les paquets

import socket
import struct
# créer le socket raw
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))


# lecture des paquets
while True:
    # lire un paquet
    raw_buffer = sniffer.recvfrom(65565)
    # analyse des en-têtes IP
    ip_header = raw_buffer[0][0:20]
    # decode the ip header
    ip_header = struct.unpack('!BBHHHBBH4s4s', ip_header)
    # affichage ip src et ip dst
    print("IP : ", ip_header[12:16], " -> ", ip_header[16:20])
    # affichage du type de protocole
    print("Protocol : ", ip_header[9])