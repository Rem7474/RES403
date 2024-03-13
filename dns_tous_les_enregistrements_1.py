import socket
def get_ips_par_recherche_dns(cible, port=None):
    if port is None:
        port = 443
    try:
        adresse_ip = socket.gethostbyname_ex(cible)
        ips = [ip for _, ip_list in adresse_ip for ip in ip_list]
        return ips
    except socket.herror:
        return None

while True:
    cible = input("Entrez un nom de domaine: ")
    if cible == "":
        break
    ip = get_ips_par_recherche_dns(cible)
    if ip:
        print(f"L'adresse IP de {cible} est {ip}")
    else:
        print(f"Impossible de trouver l'adresse IP de {cible}")