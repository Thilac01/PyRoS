import socket


class TCPTransport:

    def __init__(self, sock=None):

        if sock is None:
            self._socket = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
        else:
            self._socket = sock

    def bind(self, host, port):

        self._socket.bind((host, port))

    def listen(self, backlog=10):

        self._socket.listen(backlog)

    def accept(self):

        connection, address = self._socket.accept()

        return TCPTransport(connection), address

    def connect(self, host, port):

        self._socket.connect((host, port))

    def send(self, data):

        self._socket.sendall(data)

    def receive(self, buffer_size=4096):

        return self._socket.recv(buffer_size)

    def close(self):

        self._socket.close()