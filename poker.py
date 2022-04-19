from classes import *

def hand_value(hand):
    #ROYAL FLUSH
    for i in range(1,5):
        rf = True
        if hand.Contains(Card(Value.Ace, Suit(i))) == False:
            rf = False
        if hand.Contains(Card(Value.King, Suit(i))) == False:
            rf = False
        if hand.Contains(Card(Value.Queen, Suit(i))) == False:
            rf = False
        if hand.Contains(Card(Value.Jack, Suit(i))) == False:
            rf = False
        if hand.Contains(Card(10, Suit(i))) == False:
            rf = False
        if rf:
            return Hands.Royal_Flush
    return None