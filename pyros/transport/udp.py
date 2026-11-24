import socket


class UDPTransport:

    def __init__(self):

        self._socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

    def bind(self, host, port):

        self._socket.bind((host, port))

    def send(self, data, host, port):

        return self._socket.sendto(
            data,
            (host, port)
        )

    def receive(self, buffer_size=65535):

        data, address = self._socket.recvfrom(
            buffer_size
        )

        return data, address

    def set_timeout(self, seconds):

        self._socket.settimeout(seconds)

    def close(self):

        self._socket.close()