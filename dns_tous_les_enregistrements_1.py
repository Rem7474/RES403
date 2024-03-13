import socket
def get_ips_par_recherche_dns(cible, port=None):
    if port is None:
        port = 443
    try:
        ip_address = socket.gethostbyname(cible)
        return ip_address
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