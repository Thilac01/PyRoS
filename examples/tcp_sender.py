from pyros.transport.tcp import TCPTransport


client = TCPTransport()

client.connect("127.0.0.1", 5000)

try:

    while True:

        message = input("Enter message: ")

        if message == "exit":
            break

        client.send(message.encode())

finally:

    client.close()