from classes import *
from poker import hand_value
from tqdm import tqdm

a=0
r=0
for i in tqdm(range(3000000)):
    cards = []
    for x in range(5):
        cards.append(Card())
    if hand_value(Hand(cards)) == Hands.Royal_Flush:
        a = a + 1
    r = r + 1

print(a/r)