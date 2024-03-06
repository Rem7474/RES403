#script utilisant une socket brute pour sniffer les paquets

import socket
import struct
# créer le socket raw
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))


# lecture des paquets
while True:
    # lire un paquet
    raw_buffer = sniffer.recvfrom(65565)
    # extraire l'en-tête IP du début du paquet
    ip_header = raw_buffer[14:34]
    # dépaqueter l'en-tête IP
    iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
    # afficher les informations sur l'en-tête IP
    print ('Protocole : ' + str(iph[6]))
    print ('Source : ' + socket.inet_ntoa(iph[8]))
    print ('Destination : ' + socket.inet_ntoa(iph[9]))
