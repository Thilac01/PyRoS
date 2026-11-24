import threading

from pyros.transport.multicast import (
    MulticastTransport
)


name = input("Enter participant name: ")

transport = MulticastTransport()


def receive_loop():

    while True:

        try:

            data, address = transport.receive()

            print(
                f"\n[{address[0]}] "
                f"{data.decode()}"
            )

        except OSError:

            break


receiver_thread = threading.Thread(
    target=receive_loop,
    daemon=True
)

receiver_thread.start()

transport.send(
    f"{name} has joined".encode()
)

try:

    while True:

        message = input("Message: ")

        if message == "exit":
            break

        transport.send(
            f"{name}: {message}".encode()
        )

except KeyboardInterrupt:

    pass

finally:

    transport.close()