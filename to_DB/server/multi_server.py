import threading
import client
import atexit

from socket import *
from temp_data import TempData


class MultiServer(TempData):
    def __init__(self):
        self._max_clients = self.max_clients

        self._server_socket = socket(AF_INET, SOCK_STREAM)
        self._server_port = self.server_port

    def start_server(self):
        self._server_socket.bind(('', self._server_port))
        self._server_socket.listen(20)
        print('Server ready')

        listening_thread = threading.Thread(target=self.connections)
        listening_thread.start()

    def close_server(self):
        try:
            self._server_socket.close()
        except:
            pass

    def remove_client(self, client_):
        if client_ in self.clients:
            self.clients.remove(client_)
        del client_

    def server_member(self):
        return self._max_clients == len(TempData.clients)

    def connections(self):
        while True:
            if not self.server_member():
                conn_socket, addr = self._server_socket.accept()
                new_client = client.Client(f'temp{len(TempData.clients)+1}', conn_socket, addr)
                TempData.clients.append(new_client)
                self.send_message_to_client(conn_socket, 'connect' + self.header_split + f'temp{len(TempData.clients)+1}')
                print('connect')
                print(self.clients)
            else:
                conn_socket, addr = self._server_socket.accept()
                self.send_message_to_client(conn_socket, 'error' + self.header_split + "Server is full")
                conn_socket.close()

    def send_message_to_client(self, client_socket, message):
        packet_length = 1024
        print(message)
        if len(message.encode('UTF-8')) < packet_length:
            filled_packet = message.ljust(packet_length)
        else:
            filled_packet = message[:packet_length]
        client_socket.send(filled_packet.encode('UTF-8'))
        print('sent')


if __name__ == "__main__":
    server = MultiServer()
    server.start_server()
    atexit.register(server.close_server)
