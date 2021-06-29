#!/usr/bin/env python3

from websocket_server import WebsocketServer
import time,random

class Room:
    roomid = 0
    clients = []
    closed = False

    def __init__(self):
        id = random.uniform(100000, 999999)

    def getRoomNumber(self):
        return self.roomid

    def connection(self, address):
        if (len(self.clients) >= 2):
            self.closed = True
            return 0
        else:
            self.clients.append(address)
            return 1

class WS():
    def __init__(self, autorun):
        _PORT = 10005
        _HOST = '0.0.0.0'
        self.server = WebsocketServer(port=_PORT, host=_HOST)
        self.clients = []

        if (autorun):
            self.run()

    def new_client(self, client, server):
        print('New client : {} / given ID : {}'.format(client['address'][0], client['id']))
        self.clients.append(client)

    def client_left(self, client, server):
        print('Client left : {}'.format(client['address'][0]))

    def message_received(self, client, server, message):
        to = int(random.uniform(0, len(self.clients)-1))
        print('{}'.format(to))
        self.server.send_message(self.clients[to], 'You choosed.')

    def run(self):
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.message_received)
        self.server.run_forever()

if __name__ == "__main__":
    ws = WS(True)
