import random
from pokereval import PokerEval
class Bluffer:
    def __init__(self):
        self.wait = random.randrange(5, 10)
    def nextRound(self):
        if self.wait != 0:
            self.wait -= 1
    def reset(self):
        self.wait = random.randrange(5,10)
    def isBluff(self, bankRollState, numHands, handID):
        if self.wait == 0 or (abs(bankRollState[2]) > 75 * (numHands - handID + 1) and bankRollState[2] < 0):
           
            return True
        return False
    def bluffHandPercent(self,boardCards,POKER,leftPlayerIn,rightPlayerIn):
        maxHandScore = [0,0]

        for i in range(1,52):
            for j in range(i):
                if POKER.card2string(i) not in boardCards and POKER.card2string(j) not in boardCards:
                    curr = POKER.best_hand_value('hi', boardCards + [i,j])
                    if curr > maxHandScore[0]:
                        maxHandScore = [curr, [i,j]]

        if leftPlayerIn and rightPlayerIn:
            if len(boardCards) == 3:
                prob = float(POKER.poker_eval(game = 'holdem', pockets = [maxHandScore[1],[255,255],[255,255]], dead = [], board = boardCards + [255,255], iterations = 10000)['eval'][0]['winhi'])/10000
            elif len(boardCards) == 4:
                prob = float(POKER.poker_eval(game = 'holdem', pockets = [maxHandScore[1],[255,255],[255,255]], dead = [], board = boardCards + [255], iterations = 10000)['eval'][0]['winhi'])/10000
            else:
                prob = float(POKER.poker_eval(game = 'holdem', pockets = [maxHandScore[1],[255,255],[255,255]], dead = [], board = boardCards, iterations = 10000)['eval'][0]['winhi'])/10000

            
        else:
            if len(boardCards) == 3:
                prob = float(POKER.poker_eval(game = 'holdem', pockets = [maxHandScore[1],[255,255]], dead = [], board = boardCards + [255,255], iterations = 10000)['eval'][0]['winhi'])/10000
            elif len(boardCards) == 4:
                prob = float(POKER.poker_eval(game = 'holdem', pockets = [maxHandScore[1],[255,255]], dead = [], board = boardCards + [255], iterations = 10000)['eval'][0]['winhi'])/10000
            else:
                prob = float(POKER.poker_eval(game = 'holdem', pockets = [maxHandScore[1],[255,255]], dead = [], board = boardCards, iterations = 10000)['eval'][0]['winhi'])/10000

        return prob * .90

    def bluffHandPercentPreFlop(self):   
        prob = random.random()/4 + .6
        return prob

        
    
