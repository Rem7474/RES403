#4.1b - Filtrage par protocole

# Script capture_pcap_1.py
from scapy.all import *
# Lecture du fichier pcap capture.pcap
paquets_captures = rdpcap('capture.pcap')
# Iteration sur l’ensemble des paquets captures
for paquet in paquets_captures:
# Affichage du resume
print(paquet.summary())
# Affichage des details
paquet.show()