import socket as socket
def get_ips_par_recherche_dns(cible, port=None):
    try:
        ip_address = socket.gethostbyname(cible)
        print("IP address of the host: ", ip_address)
    except socket.herror:
        print("No DNS record found")
#set dns server
hostname="iut-acy.local"
try:
    hostname, aliaslist, ipaddrlist = socket.gethostbyaddr("10.108.239.251")
    print(hostname, aliaslist, ipaddrlist)
except socket.herror:
    print("No DNS record found")

try:
    dns, alias, prout= socket.gethostbyname_ex(hostname)
    print(dns, alias, prout)
except socket.herror:
    print("No DNS record found")