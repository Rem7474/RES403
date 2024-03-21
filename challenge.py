#script pour analyser un fichier pcapng

#import des librairies
import scapy.all as scapy

#ouverture du fichier pcapng
file = scapy.rdpcap("capture.pcapng")

#affichage des paquets
user="juizegefupazg"
nb_packet=0
nb1=100000
nb2=100000
trouve=False
for packet in file:
    #recherche de "USER" dans les data des paquets
    if "USER" in str(packet.load):
        #print(packet.load)
        user=packet.load.decode('utf-8')
        print(user)
        nb=nb_packet
    if "PASS" in str(packet.load):
        #print(packet.load)
        password=packet.load.decode('utf-8')
        print(password)
        nb2=nb_packet
    if user in str(packet.load):
        #print(packet.load)
        print(packet.load.decode('utf-8'))
    if nb_packet>nb2+5 and nb_packet<nb2+20:
        #print(packet.load)
        #test si la requète contient .pdf
        if ".pdf" in str(packet.load):
            #print(packet.load)
            trouve=True
    #test si la trames est de type FTP-DATA et enregistrement du fichier (de toutes les trames FTP-DATA) dans un fichier pdf
    if packet.haslayer(scapy.Raw) and packet.haslayer(scapy.TCP) and packet[scapy.TCP].dport==21:
        #print(packet.load)
        if "RETR" in str(packet.load):
            #print(packet.load)
            print(packet.load.decode('ascii'))
    #enregistrement du paquet retour dans un fichier pdf
    if packet.haslayer(scapy.Raw) and packet.haslayer(scapy.TCP) and packet[scapy.TCP].sport==21:
        #print(packet.load)
        if ".pdf" in str(packet.load):
            #print(packet.load)
            print(packet.load.decode('ascii'))
    if packet.haslayer(scapy.Raw) and packet.haslayer(scapy.TCP) and packet[scapy.TCP].sport==20:
        #print(packet.load)
        #ajout des données ftp data dans le fichier pdf
        #écriture dans le fichier
        file = open("fichier.pdf", "ab")
        file.write(packet.load)
        file.close()
        
        
    nb_packet+=1


