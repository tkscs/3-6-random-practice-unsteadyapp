suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
import random
deck = []
for j in range(len(suits)):
    for i in range(len(values)):
        deck.append(f"{values[i]}{suits[j]}")
print(deck)
# Make a deck of cards
# `deck` should be a list of strings with a value and a suit, e.g. "4♣"

#shuffle your `deck` and print it out
random.shuffle(deck)
hand = deck[0:5]
print(hand)
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
    numbersOnly.sort()
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
    return toReturn
def whatpokerhand(hand):
    newHand = []
    for i in hand:
        newHand.append(f"{values.index(i[0])+1}{i[1]}")
    print(newHand)
    straight = isStraight(newHand)
    flush = isFlush(newHand)
    reduceToInt(highestpair)
    if(straight and flush and False):
        pass
    elif(straight and flush):
        print("stright flush")


    #flush = isFlush(hand)
    #if(hand): 
whatpokerhand(['3f', '5♦', '6♦', '7♦', '8♦'])


# sample a hand of 5 cards and print it out
# (WITHOUT replacement -- no repeats!)