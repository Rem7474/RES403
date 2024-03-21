import socket
import ssl
import sslkeylog
import os

#openssl genrsa -out ca.key 2048
#openssl req -new -x509 -days 365 -key ca.key -out ca.pem

#openssl genrsa -out server.key 2048
#openssl req -new -key server.key -out server.csr
#openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out server.pem

#openssl genrsa -out client.key 2048
#openssl req -new -key client.key -out client.csr
#openssl x509 -req -days 365 -in client.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out client.pem


pemServer = "ca.pem"
pemClient = "client.pem"
keyClient = "client.key"

sslkeylog.set_keylog("SSLKEYLOGFILE")

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
context.verify_mode = ssl.CERT_NONE
context.load_verify_locations(pemServer)
context.load_cert_chain(certfile=pemClient, keyfile=keyClient)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = context.wrap_socket(client)
client.connect(('127.0.0.1', 4443))

print(sslkeylog.set_keylog(context))

client.send(bytes("Client --> Hi, Praneeth Here ...\n", encoding='utf8'))

from_server = str(client.recv(4096),encoding='utf8')
print(from_server)

client.close()