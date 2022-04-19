from enum import Enum
from random import randrange
class Suit(Enum):
    Clubs = 1
    Spades = 2
    Hearts = 3
    Diamonds = 4

class Value(Enum):
    King = 13
    Queen = 12
    Jack = 11
    Ace = 1

class Hands(Enum):
    Royal_Flush = 1
    Straight_Flush = 2
    Four = 3
    Full_House = 4
    Flush = 5
    Straight = 6
    Three = 3
    Two_Pair = 8
    Pair = 9
    High_Card = 10

class Card:
  def __init__(self, value=-99, suit=-99):
    self.value = value
    self.suit = suit
    if value == -99:
        val = randrange(1,14)
        if val > 10 or val == 1:
           self.value = Value(val)
        else:
            self.value = val 
        self.suit = Suit(randrange(1,5))
  def __str__(self):
    if type(self.value) == int:
        return str(self.value) + " of " + str(self.suit.name)
    else:
        return str(self.value.name) + " of " + str(self.suit.name)
  def Value(self):
      if type(self.value) == int:
        return int(self.suit.value)*int(self.value)
      else:
        return int(self.suit.value)*int(self.value.value)
class Hand:
    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        retstring = ""
        for card in self.cards:
            retstring = retstring + str(card) + " | " + " "
        return retstring[:-1]
    def List(self):
        return self.cards
    def Contains(self, target):
        for card in self.cards:
            if card.Value() == target.Value():
                return True
            return False
