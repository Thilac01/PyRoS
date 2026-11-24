from pyros.transport.tcp import TCPTransport


server = TCPTransport()

server.bind("127.0.0.1", 5000)

server.listen()

print("PyROS TCP server started")

connection, address = server.accept()

print("Connected:", address)

try:

    while True:

        data = connection.receive()

        if not data:
            break

        print("Received:", data.decode())

finally:

    connection.close()
    server.close()