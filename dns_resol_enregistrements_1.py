import socket as socket
#set dns server
ip_address="10.108.239.251"
try:
    hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip_address)
    print(hostname, aliaslist, ipaddrlist)
except socket.herror:
    print("No DNS record found")