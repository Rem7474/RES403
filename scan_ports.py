#2.2 Scan de ports : scan TCP
from scapy.all import sr1,IP,conf,TCP

#script pour effectué un scan sur tout les ports d'une machine
def tcp_scan(hote, port):
    # Envoi du paquet SYN et réception de la réponse
    paquet_syn = IP(dst=hote) / TCP(dport=port, flags="S")
    reponse_syn = sr1(paquet_syn, verbose=False, timeout=1)

    if reponse_syn is None:
        return "Port {} : Filtré / Aucune réponse reçue".format(port)
    elif reponse_syn.haslayer(TCP) and reponse_syn.getlayer(TCP).flags == 0x12:
        return "Port {} : Ouvert".format(port)
    elif reponse_syn.haslayer(TCP) and reponse_syn.getlayer(TCP).flags == 0x14:
        return "Port {} : Fermé".format(port)
    else:
        return "Port {} : État inconnu".format(port)

# Hôte cible
hote = input("Entrez l'adresse IP de la cible : ")

# Désactiver les messages d'avertissement
conf.verb = 0

# Scanner tous les ports courants
for port in range(1, 1025):
    resultat = tcp_scan(hote, port)
    print(resultat)