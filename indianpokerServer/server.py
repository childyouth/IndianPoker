import socketserver
from userManager import UserManager


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class TcpHandler(socketserver.BaseRequestHandler):
    manager = UserManager()

    def handle(self):
        username = ''

        try:
            username = self.registerUsername()
            print('[%s][%s] 연결됨' %(self.client_address[0],username))

            while True:
                msg = self.request.recv(1024)
                if self.manager.messageHandler(username, msg.decode()) == -1:
                    self.request.close()
                    break

        except Exception as e:
            print(e)

        print('[%s][%s] 접속종료' %(self.client_address[0],username))
        self.manager.removeUser(username)

    def registerUsername(self):
        while True:
            msg = self.request.recv(1024)
            msg = msg.decode().strip()
            msg = msg.split('\\')
            username = msg[0]
            roomnum = msg[1]
            if self.manager.addUser(username, roomnum, self.request, self.client_address):
                return username