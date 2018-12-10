import socket
from threading import Thread
from PyQt5.QtCore import *

PORT = 8001

class Communication(QObject):
    sender_signal = pyqtSignal(str)
    def __init__(self, CALLBACK,id,room_num,HOST):
        super().__init__()
        print(HOST)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST.encode(), PORT))
            self.sender = Sender(sock)
            self.receiver = Receiver(sock)
            self.receiver.message_received.connect(CALLBACK)
            self.sender_signal.connect(self.sender.msgSend)
            self.receiver.start()
        except Exception as e:
            print("")
            print(e)
        try:
            self.send(id + "\\" + room_num)
        except Exception as e:
            print(e)

    def send(self,msg):
        self.sender_signal.emit(msg)

class Sender:
    def __init__(self,sock):
        self.sock = sock

    def msgSend(self,msg):
        try:
            self.sock.send(msg.encode())
        except Exception as e:
            print(e)

class Receiver(QThread):
    message_received = pyqtSignal(str)
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            try:
                data = self.sock.recv(1024).decode()
                self.message_received.emit(data)
            except:
                print("연결끊김")
                break