from pyros.transport.udp import UDPTransport


sender = UDPTransport()

try:

    while True:

        message = input("Enter message: ")

        if message == "exit":
            break

        sender.send(
            message.encode(),
            "127.0.0.1",
            5001
        )

finally:

    sender.close()