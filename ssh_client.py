import socket
import ssl
import sslkeylog
import os
pemServer = "ca.pem"
pemClient = "client.pem"
keyClient = "client.key"

sslkeylog.set_keylog("SSLKEYLOGFILE")

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(pemServer)
context.load_cert_chain(certfile=pemClient, keyfile=keyClient)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = context.wrap_socket(client)
client.connect(('127.0.0.1', 4433))

print(sslkeylog.set_keylog(context))

client.send(bytes("Client --> Hi, Praneeth Here ...\n", encoding='utf8'))

from_server = str(client.recv(4096),encoding='utf8')
print(from_server)

client.close()