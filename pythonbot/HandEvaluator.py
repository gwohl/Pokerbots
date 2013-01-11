def discard(POKER, hand, board):
    h = hand
    possibleHands = [[h[1],h[2]],[h[0],h[2]],[h[0],h[1]]]
    bestHand = 0
    bestEq = 0
    for i in xrange(3):
        eq = twoCardPostFlopEquity(possibleHands[i],h[i],board) # DEFINE THIS FUNCTION!!!!!
        if eq > bestEq:
            bestEq = eq
            bestHand = i
    discarded = h.pop(i) 
    return discarded,h

def twoCardPostFlopEquity(POKER, hand, discardedCard, boardCards):
    prob = float(POKER.poker_eval(game = 'holdem',
                                  pockets = [hand, [255, 255]],
                                  dead = [discardedCard],
                                  board = boardCards,
                                  iterations = 1000)['eval'][0]['winhi'])/1000
                                  
    return prob

def postFlopEquity(hand, discardedCard, boardCards):
    return 0.0

