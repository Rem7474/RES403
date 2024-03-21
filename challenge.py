#script pour analyser un fichier pcapng

#import des librairies
import pyshark

#ouverture du fichier pcapng
cap = pyshark.FileCapture('capture.pcapng')

#recherche d'un paquet contenant "user" dans les données
for packet in cap:
    if 'USER' in str(packet.data):
        print(packet.data)
        break
    
#fermeture du fichier pcapng
cap.close()