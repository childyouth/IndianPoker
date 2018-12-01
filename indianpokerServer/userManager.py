import threading
from game import Game

lock = threading.Lock()

class UserManager:

    def __init__(self):
        self.users = {}
        self.rooms = {}
        self.gameManager = {}

    def addUser(self, username, roomnum, conn, addr):
        if username in self.users:
            conn.send('이미 등록된 사용자입니다.'.encode())
            return None
        if roomnum in self.rooms:
            if len(self.rooms[roomnum]) == 1:
                conn.send("/enter".encode())
                lock.acquire()
                self.rooms[roomnum] += [username]
                lock.release()
            else:
                conn.send("이미 게임중인 방입니다.".encode())
                return None
        else:
            conn.send("/enter".encode())
            lock.acquire()
            self.rooms[roomnum] = [username]
            lock.release()

        lock.acquire()
        self.users[username] = (conn, addr, roomnum)
        lock.release()

        self.sendMessage('[%s]님이 입장했습니다.' % username,roomnum)
        if len(self.rooms[roomnum]) == 2:
            self.sendMessage("/game",roomnum)

        return username

    def removeUser(self, username):
        if username not in self.users:
            return

        roomnum = self.users[username][2]

        lock.acquire()
        del self.users[username]
        self.rooms[roomnum].remove(username)
        lock.release()

        self.sendMessage('[%s]님이 퇴장했습니다.' % username,roomnum)

    def messageHandler(self, username, msg):
        roomnum = self.users[username][2]
        print(msg)
        if msg.strip() == '/game':
            print(str(roomnum) + "번 방 게임시작")
            lock.acquire()
            self.gameManager[roomnum] = Game(self.rooms[roomnum])
            lock.release()
            return

        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1

    def sendMessage(self, msg, room):
        for conn, addr, roomnum in self.users.values():
            if room == roomnum:
                conn.send(msg.encode())