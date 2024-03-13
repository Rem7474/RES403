#2.2 Scan de ports : scan TCP
import sr1,IP,TCP,conf

#script pour effectué un scan sur tout les ports d'une machine
#on envoie un paquet TCP SYN sur chaque port
#si on recoit un pajson SYN/ACK, le port est ouvert
#si on recoit un paquet RST, le port est fermé
#si on recoit un paquet ICMP, le port est filtré

#on désactive les messages de scapy
conf.verb=0

ip=input("Entrez l'adresse IP de la machine à scanner : ")
#on crée un paquet IP
paquet=IP(dst=ip)
#on crée un paquet TCP
tcp=TCP(dport=(1,1024),flags="S")
#on envoie le paquet
reponse=sr1(paquet/tcp)
#on analyse la réponse
if reponse.haslayer(TCP):
    port=reponse[TCP].sport
    if reponse[TCP].flags==18:
        print("Port ouvert : ",port)
    elif reponse[TCP].flags==20:
        print("Port fermé")
    else:
        print("Port filtré")
else:
    print("Pas de réponse")
