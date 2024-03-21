#script pour analyser un fichier pcapng

#import des librairies
import scapy.all as scapy

#ouverture du fichier pcapng
file = scapy.rdpcap("capture.pcapng")

#affichage des paquets
user=""
for packet in file:
    #recherche de "USER" dans les data des paquets
    if "USER" in str(packet.load):
        user=packet.load.decode('utf-8')
        print(user)
    if "PASS" in str(packet.load):
        password=packet.load.decode('utf-8')
    if user in str(packet.load):
        print(packet.load.decode('utf-8'))
        break
    


