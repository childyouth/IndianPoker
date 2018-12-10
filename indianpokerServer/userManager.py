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
            conn.send('/id_taken\\'.encode())
            return None
        if roomnum in self.rooms:
            if len(self.rooms[roomnum]) == 1:
                print(username + " < enter")
                conn.send("/enter\\".encode())
                lock.acquire()
                self.rooms[roomnum] += [username]
                lock.release()
            else:
                conn.send("/room_num_taken\\".encode())
                return None
        else:
            print(username + " < enter")
            conn.send("/enter".encode())
            lock.acquire()
            self.rooms[roomnum] = [username]
            lock.release()

        lock.acquire()
        self.users[username] = (conn, addr, roomnum)
        lock.release()

        self.sendMessage('/msg [%s]님이 입장했습니다.' % username,roomnum)
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
            try:
                tmp = self.gameManager[roomnum]
            except KeyError:
                lock.acquire()
                self.gameManager[roomnum] = Game(self.rooms[roomnum])
                lock.release()
            self.users[username][0].send(('/next_turn ' + self.gameManager[roomnum].user_data_json(username)).encode())
            order = ''
            if self.gameManager[roomnum].get_attack_first() == username:
                order = '/bet\\'
            else:
                order = '/wait_for_bet\\'
            self.users[username][0].send(order.encode())
            return

        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1

    def sendMessage(self, msg, room):
        for conn, addr, roomnum in self.users.values():
            if room == roomnum:
                conn.send((msg + "\\").encode())