#script pour analyser un fichier pcapng

#import des librairies
import scapy.all as scapy

#ouverture du fichier pcapng
file = scapy.rdpcap("capture.pcapng")

#affichage des paquets
for packet in file:
    print(packet.show())


