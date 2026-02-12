suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
import random
import matplotlib.pyplot as plt
deck = []

for j in range(len(suits)):
    for i in range(len(values)):
        deck.append(f"{values[i]}{suits[j]}")
# Make a deck of cards
# `deck` should be a list of strings with a value and a suit, e.g. "4♣"

#shuffle your `deck` and print it out
def isFlush(hand):
    toReturn = True
    suit = ""
    for i in hand:
        if(suit == ""):
            suit = i[-1]
        elif(suit != i[-1]):
            toReturn = False
        suit = i[-1]
    return toReturn
def isStraight(hand):
    toReturn = False
    numbersOnly = reduceToInt(hand,True)
    consec = 0
    for i in range(len(numbersOnly)):
        if(consec == 0):
            consec+=1
        else:
            if(numbersOnly[i] == numbersOnly[i-1] + 1):
                consec+=1
                if(consec > 4):
                    toReturn= True
            else:
                consec = 0
    return(toReturn)
def reduceToInt(list,toInt = True):
    toReturn = []
    for i in list:
        if(toInt):
            toReturn.append(int(i[:-1]))
        else:
            toReturn.append(i[:-1])
    toReturn.sort()
    return toReturn
def whatpokerhand(hand):
    newHand = []
    for i in hand:
        newHand.append(f"{values.index(i[:-1])+1}{i[-1]}")
    straight = isStraight(newHand)
    flush = isFlush(newHand)
    reduced = reduceToInt(newHand)
    numbers = []
    for i in list(set((reduced.copy()))):
        numbers.append(reduced.count(i))
    maxed= max(numbers)
    if(straight and flush and False):
        pass
    elif(straight and flush):
        return("stright flush")
    elif(maxed>3):
        return("Four of a kind")
    elif((3 in numbers) and (2 in numbers)):
        return("full house")
    elif(flush):
        return("Flush")
    elif(straight):
        return(straight)
    elif(maxed > 2):
        return("three of a kind")
    elif((2 == numbers.count(2))):
        return "two pair"
    elif(maxed > 1):
        return("pair")
    else:
        return("high card")
    #flush = isFlush(hand)
    #if(hand): 
#print(whatpokerhand(['1♦', '3♦', '3♦', '3♦', '3♦']))
data = []
sample = 1000
for i in range(sample):
    random.shuffle(deck)
    hand = deck[0:5]
    pokerhand = whatpokerhand(hand)
    data.append(pokerhand)
    #print(hand,pokerhand)
counts = []
hands = []
print(data)
for i in list(set(data.copy())):
    hands.append(i)
    counts.append(data.count(i))

fig, ax = plt.subplots()
bar_colors = []
for i in range(len(hands)):
    bar_colors.append("tab:blue")


ax.bar(hands, counts, label=hands, color=bar_colors)

ax.set_ylabel('Number of hands')
ax.set_title(f'Poker hands by probablity in a 1000')
ax.legend(title='Poker Hands')
plt.show()
# sample a hand of 5 cards and print it out
# (WITHOUT replacement -- no repeats!)