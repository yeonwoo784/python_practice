import random


NUM_CARDS_PER_SHAPE = 13
NUM_SHAPES = 4
NUM_CARDS = NUM_SHAPES * NUM_CARDS_PER_SHAPE


class Card:
    def __init__(self, index):
        self.shape = index / 13 #모양결정
        self.value = index % 13 + 1 #A=1부터 K=13까지 (game.py에서 알파벳 전부 10으로 바뀜)


class Deck:
    def __init__(self, num_sets=1):
        self.cards = [Card(i) for i in range(NUM_CARDS)] * num_sets
        self.shuffle() #52개가 서로 섞여있음.
        self.next = 0

    def draw(self):
        card = self.cards[self.next] #next로 인덱스 하나씩 늘려주면서 카드가 바뀌는 구조.
        self.next = self.next + 1
        if self.next == len(self.cards): #52개 카드 다씀
            self.next = 0
            self.shuffle() #카드 다시 다 넣고 다시 셔플
        return card

    def shuffle(self):
        random.shuffle(self.cards)