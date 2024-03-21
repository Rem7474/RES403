import socket
import ssl
#openssl genrsa -out server.key 2048
#openssl req -new -key server.key -out server.csr
#openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out server.pem
#openssl genrsa -out ca.key 2048
#openssl req -new -x509 -days 365 -key ca.key -out ca.pem

pemServer = "ca.pem"
keyClient = "server.key"
pemClient = "server.pem"

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(pemServer)
context.load_cert_chain(certfile=pemClient, keyfile=keyClient)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv = context.wrap_socket(serv)

serv.bind(("127.0.0.1", 4443))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        data = str(conn.recv(4096), encoding='utf8') # The received data type is byte, converted to str
        if not data:
            break
        from_client = from_client + data
        print(from_client)

        conn.send(bytes("Server --> Hi Praneeth, How are you doing ?\n",encoding='utf8')) # Convert str to byte type, you need to use byte when transmitting

    conn.close()