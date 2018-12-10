import random
import json

class Game:
    def __init__(self, users):
        self.deck_shuffle()
        self.user = {}
        self.user1 = users[0]
        self.user2 = users[1]
        self.user[self.user1] = dict()
        self.user[self.user2] = dict()
        self.user[self.user1]["money"] = 10000
        self.user[self.user2]["money"] = 10000
        self.give_cards()
        self.attack_first = random.choice([self.user1,self.user2])
        self.bet = 0

    def get_attack_first(self):
        return self.attack_first

    def deck_shuffle(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
        random.shuffle(self.deck)

    def give_cards(self):
        if len(self.deck) <= 0:
            self.deck_shuffle()
        self.user['deck_len'] = len(self.deck)
        self.user[self.user1]["card"] = self.deck.pop()
        self.user[self.user2]["card"] = self.deck.pop()

    def data_json(self):
        return json.dumps(self.user)

    def user_data_json(self, username):
        tmp = dict()
        if username == self.user1:
            opponent = self.user2
        else:
            opponent = self.user1
        tmp[username] = {"money":self.user[username]["money"]}
        tmp[opponent] = self.user[opponent]
        return json.dumps(tmp)

    def get_winner(self):
        draw = "draw"
        if self.user[self.user1]["card"] > self.user[self.user2]["card"]:
            self.attack_first = self.user1
            return self.user1
        elif self.user[self.user1]["card"] < self.user[self.user2]["card"]:
            self.attack_first = self.user2
            return self.user2
        else:
            return draw