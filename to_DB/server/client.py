import threading
import os
from temp_data import TempData
from read_db import InteractionToDB


class Client(TempData, InteractionToDB):

    def __init__(self, name, connection, address):
        self._client_name = name
        self._client_socket = connection
        self._client_address = address
        self._exist = True

        receiving_thread = threading.Thread(target=self.receive_from_client, daemon=True)
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
                self._client_socket.close()
                print('disconnect')

        elif command == 'file':
            name = parsed[1].strip()
            self.send_file(name)

        elif command == 'district':
            self.district_list = self.get_district()
            district = self.list_split_1.join(self.district_list)
            self.send_to_client('district' + self.header_split + district)

        elif command == 'local':
            district = parsed[1].strip()
            local_list = self.get_local(district)
            _local = self.list_split_1.join(local_list)
            self.send_to_client('local' + self.header_split + _local)

        elif command == 'data':
            data_list = self.list_split_1.join(self.data_list)
            self.send_to_client('data' + self.header_split + data_list)

        elif command == 'scan':
            para_list = parsed[1][0].strip()
            para = self.list_split_1.join(para_list)
            data = self.data_scan(para)
            self.send_to_client('scan' + self.header_split + data)

    def send_file(self, name):
        path = f'../db/send/{name}'
        file_size = self.get_file_size(path)
        self.send_to_client('size' + self.header_split + file_size)
        with open(path, 'rb') as file:
            try:
                data = file.read()
                self._client_socket.sendall(data)
                file.close()
                print('file sent')

            except Exception as ex:
                print(ex)

    def get_file_size(self, path):
        file_size = os.path.getsize(path)
        return str(file_size)
