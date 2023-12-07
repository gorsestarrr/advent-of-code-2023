from collections import defaultdict
from functools import cmp_to_key


class Card:
    def __init__(self, value):
        self.value = value

    def comparator(self, other):
        if self.value == other.value:
            return 0
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        return 1 if cards.index(self.value) > cards.index(other.value) else -1

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return self.value

    def __iter__(self):
        return iter(self.value)

    def __eq__(self, other):
        return self.comparator(other) == 0

    def __lt__(self, other):
        return self.comparator(other) == -1

    def __gt__(self, other):
        return self.comparator(other) >= 1




class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def __repr__(self):
        return {'cards': self.cards, 'bid': self.bid}

    def get_type(self):
        map = defaultdict(int)
        for c in self.cards:
            map[c] += 1
        if len(map.keys()) == 1:
            return 6
        if len(map.keys()) == 2:
            return 5 if max(list(map.values())[0], list(map.values())[1]) == 4 else 4
        if len(map.keys()) == 3:
            return 3 if max(list(map.values())[0], list(map.values())[1], list(map.values())[2]) == 3 else 2
        if len(map.keys()) == 4:
            return 1
        return 0

    def comparator(a, b):
        if a.get_type() > b.get_type():
            return 1
        if a.get_type() < b.get_type():
            return -1
        for i in range(len(a.cards)):
            if a.cards[i] == b.cards[i]:
                continue
            if a.cards[i] > b.cards[i]:
                return 1
            return -1


def parse(file):
    lines = file.readlines()
    decks = []
    for line in lines:
        parsed = line.strip().split(" ")
        cards = [Card(char) for char in parsed[0]]
        bid = int(parsed[1])
        decks.append(Hand(cards, bid))
    return decks


def part1(decks):
    decks = sorted(decks, key=cmp_to_key(Hand.comparator))
    rv = 0
    for i, deck in enumerate(decks):
        rv += deck.bid * (i + 1)
    return rv


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        decks = parse(file)
        print(part1(decks))