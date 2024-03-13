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
    ip_header = raw_buffer[0][14:34]
    # dépaqueter l'en-tête IP
    iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
    data={'Protocole':iph[6],'Source':socket.inet_ntoa(iph[8]),'Destination':socket.inet_ntoa(iph[9])}
    msg="| type de protocole: %s | Source: %s | Destination: %s |" % (data['Protocole'], data['Source'], data['Destination'])
    print("-"*len(msg))
    print(msg)
    print("-"*len(msg))