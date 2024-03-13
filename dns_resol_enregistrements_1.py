import socket as socket
print("Résolution IP")
try:
    hostname, aliaslist, ipaddrlist = socket.gethostbyaddr("10.108.239.251")
    print(hostname, aliaslist, ipaddrlist)
except socket.herror:
    print("No DNS record found")


print("Résolution nom de domaine")
hostname="iut-acy.local"
try:
    dns, alias, prout= socket.gethostbyname_ex(hostname)
    print(dns, alias, prout)
    #affichage de l'ip du server DNS
    print(f"Adresse du serveur DNS : {socket.gethostbyname(dns)}")
except socket.herror:
    print("No DNS record found")