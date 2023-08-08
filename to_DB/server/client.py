import temp_data
import threading


class Client(temp_data.TempData):

    def __init__(self, name, connection, address):
        self._client_name = name
        self._client_socket = connection
        self._client_address = address
        self._exist = True

        receiving_thread = threading.Thread(target=self.receive_from_client)
        receiving_thread.start()

    def get_name(self):
        return self._client_name

    def send_to_client(self, data: str):
        packet_length = 1024
        print(data)
        if len(data.encode('UTF-8')) < packet_length:
            filled_packet = data.ljust(packet_length)
        else:
            filled_packet = data[:packet_length]
        self._client_socket.send(filled_packet.encode('UTF-8'))
        print('sent')

    def receive_from_client(self):
        try:
            while self._exist:
                packet = self._client_socket.recv(1024).decode('UTF-8')
                self.parse_packet(packet)
                print(packet)
                print('receive')
        except:
            self.parse_packet(f'disconnect{self.header_split}')

    def parse_packet(self, parce: str):

        parsed = parce.split(self.header_split)
        command = parsed[0].strip()

        if command == 'disconnect':
            if self._exist:
                self._exist = False
                # self.input_server_log('logout', self._client_name)
                self._client_socket.close()
