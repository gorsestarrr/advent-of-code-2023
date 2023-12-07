from collections import defaultdict
from functools import cmp_to_key


class Card:
    def __init__(self, value, joker_mode):
        self.value = value
        self.joker_mode = joker_mode

    def comparator(self, other):
        if self.value == other.value:
            return 0
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        j_pos = 9
        if self.joker_mode:
            j_pos = 0
        cards.insert(j_pos, 'J')
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
        if self.cards[0].joker_mode:
            if ''.join([char.value for char in self.cards]) == 'JJJJJ':
                return 6
            max_item = max(((k, v) for k, v in map.items() if k.value != 'J'), key=lambda x: x[1])
            to_remove = []
            for key in map.keys():
                if key.value == 'J':
                    map[max_item[0]] += map[key]
                    to_remove.append(key)
            map = {key: value for key, value in map.items() if key not in to_remove}
        if len(map.keys()) == 1:
            return 6
        if len(map.keys()) == 2:
            return 5 if max(list(map.values())[0], list(map.values())[1]) == 4 else 4
        if len(map.keys()) == 3:
            return 3 if max(list(map.values())[0], list(map.values())[1], list(map.values())[2]) == 3 else 2
        if len(map.keys()) == 4:
            return 1
        return 0

    @staticmethod
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


def parse(data, joker_mode):
    decks = []
    for line in data:
        parsed = line.strip().split(" ")
        cards = [Card(char, joker_mode) for char in parsed[0]]
        bid = int(parsed[1])
        decks.append(Hand(cards, bid))
    return decks

def part1(data):
    return solve(data, False)

def part2(data):
    return solve(data, True)

def solve(data, joker_mode):
    decks = parse(data, joker_mode)
    decks = sorted(decks, key=cmp_to_key(Hand.comparator))
    rv = 0
    for i, deck in enumerate(decks):
        rv += deck.bid * (i + 1)
    return rv

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
      data = file.readlines()
      print(part2(data))