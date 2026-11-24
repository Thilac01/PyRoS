from pyros.transport.udp import UDPTransport


receiver = UDPTransport()

receiver.bind("127.0.0.1", 5001)

print("PyROS UDP receiver started")

try:

    while True:

        data, address = receiver.receive()

        print(
            f"Received from {address}: "
            f"{data.decode()}"
        )

except KeyboardInterrupt:

    print("\nReceiver stopped")

finally:

    receiver.close()