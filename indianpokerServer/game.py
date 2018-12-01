import random

class Game:
    def __init__(self, users):
        self.deck = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        random.shuffle(self.deck)
        self.user = {}
        self.user1 = users[0]
        self.user2 = users[1]
        self.user[self.user1] = []
        self.user[self.user2] = []