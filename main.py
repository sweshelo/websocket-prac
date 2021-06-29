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

def start():
    def new_client(client, server):
        print('New client {}:{} has joined.'.format(client['address'][0], client['address'][1]))
        time.sleep(2)
        # クライアントへメッセージ送信
        server.send_message(client, 'from server 1st message in new_client')
        time.sleep(2)
        # クライアントへメッセージ送信
        server.send_message(client, 'from server 2st message in new_client')
 
    # クライアントが切断した時のイベント
    def client_left(client, server):
        print('Client {}:{} has left.'.format(client['address'][0], client['address'][1]))
 
    # クライアントからのメッセージを受信した時のイベント
    def message_received(client, server, message):
        print(message)

        if (message != "COM:"):
            room = Room()
            print(room.roomid)

        time.sleep(2)
        # クライアントへメッセージ送信
        server.send_message(client, 'Hi')
 
    # 10005番ポートでサーバーを立ち上げる
    server = WebsocketServer(port=10005, host='0.0.0.0')
    # イベントで使うメソッドの設定
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    # 実行
    server.run_forever()
 
if __name__ == "__main__":
    start()
