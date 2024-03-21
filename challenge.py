#script pour analyser un fichier pcapng

#import des librairies
import scapy.all as scapy

#ouverture du fichier pcapng
file = scapy.rdpcap("capture.pcapng")

#affichage des paquets
for packet in file:
    #recherche de "USER" dans les data des paquets
    if "USER" in packet.load:
        print(packet.load)


