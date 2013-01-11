def discard(hand, board):
    possibleHands = [[hand[1],hand[2]],[hand[0],hand[2]],[hand[0],hand[1]]]
    bestHand = 0
    bestEq = 0
    for i in xrange(3):
        eq = twoCardPostFlopEquity(possibleHands[i],hand[i],board) # DEFINE THIS FUNCTION!!!!!
        if eq > bestEq:
            bestEq = eq
            bestHand = i
    discarded = hand.pop(i) 
    return discarded,hand

def twoCardPostFlopEquity(hand, discardedCard, boardCards):
    return 0.0

def postFlopEquity(hand, discardedCard, boardCards):
    return 0.0
