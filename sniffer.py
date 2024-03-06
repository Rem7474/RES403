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
    version, header_length, ttl, proto, src, target, data = struct.unpack('!BBHHHBBH4s4s', raw_buffer[0][14:34])
    # affichage ip src et ip dst
    print("IP : ", src, " -> ", target)
    # affichage du type de protocole
    print("Protocol : ", proto)