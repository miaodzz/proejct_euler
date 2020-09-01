# 参考 https://www.cnblogs.com/metaquant/p/11846933.html

mp = {str(i): i for i in range(2, 10)}
appendix = ['C', 'S', 'D', 'H']
mp['T'] = 10
mp['J'] = 11
mp['Q'] = 12
mp['K'] = 13
mp['A'] = 14

from functools import cmp_to_key
from collections import Counter

class Card:
    def __init__(self,poker):
        self.num=mp[poker[0]]
        self.suit=poker[1]

    def __lt__(self, other):
        return self.num < other.num

class Hand:
    def __init__(self,pokers):
        self.cards=list(sorted([Card(s) for s in pokers]))[::-1]
        self.nums=[card.num for card in self.cards]
        self.suits=[card.suit for card in self.cards]
        self.num_counter=Counter(self.nums).most_common()
        self.suit_counter=Counter(self.suits).most_common()
        self.suit_cnts=len(set(self.suits))
        self.diff = set([self.nums[i]-self.nums[i+1] for i in range(4)])

    def categories(self):
        if self.suit_cnts == 1 and self.diff == {1}:
            return ('Straight Flush', 9)
        if self.num_counter[0][1] == 4:
            return ('Four of a Kind', 8)
        if self.num_counter[0][1] == 3 and self.num_counter[1][1] == 2:
            return ('Full House', 7)
        if self.suit_cnts == 1:
            return ('Flush', 6)
        if self.diff == {1}:
            return ('Straight', 5)
        if self.num_counter[0][1] == 3 and self.num_counter[1][1]==1:
            return ('Three of a Kind', 4)
        if self.num_counter[0][1]==2 and self.num_counter[1][1]==2:
            return ('Two Pairs', 3)
        if self.num_counter[0][1] == 2:
            return ('One Pair', 2)
        return ('High Card', 1)

    def is_winner(self, hand):
        if self.categories()[1] > hand.categories()[1]:
            return True
        if self.categories()[1] < hand.categories()[1]:
            return False
        if self.categories()[1] in [8, 7, 4, 3, 2]:
            return self.num_counter > hand.num_counter
        return self.nums > hand.nums

def main():
    count = 0
    with open('p054_poker.txt') as f:
        hands = [line.split() for line in f]
    for hand in hands:
        p1_hand,p2_hand = Hand(hand[:5]),Hand(hand[5:])
        if p1_hand.is_winner(p2_hand):
            count += 1
    print(count)

main()

# 坑 许多表意不明