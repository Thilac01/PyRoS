import socket


class MulticastTransport:

    def __init__(
        self,
        group="239.255.42.99",
        port=7400,
        interface="0.0.0.0",
        ttl=1
    ):

        self.group = group
        self.port = port
        self.interface = interface

        self._socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
            socket.IPPROTO_UDP
        )

        self._socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        self._socket.bind(("", self.port))

        self._membership = (
            socket.inet_aton(self.group)
            + socket.inet_aton(self.interface)
        )

        self._socket.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            self._membership
        )

        self._socket.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_MULTICAST_TTL,
            ttl
        )

        self._socket.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_MULTICAST_LOOP,
            1
        )

        if self.interface != "0.0.0.0":

            self._socket.setsockopt(
                socket.IPPROTO_IP,
                socket.IP_MULTICAST_IF,
                socket.inet_aton(self.interface)
            )

    def send(self, data):

        return self._socket.sendto(
            data,
            (self.group, self.port)
        )

    def receive(self, buffer_size=65535):

        return self._socket.recvfrom(
            buffer_size
        )

    def set_timeout(self, seconds):

        self._socket.settimeout(seconds)

    def close(self):

        try:

            self._socket.setsockopt(
                socket.IPPROTO_IP,
                socket.IP_DROP_MEMBERSHIP,
                self._membership
            )

        finally:

            self._socket.close()