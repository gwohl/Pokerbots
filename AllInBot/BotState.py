import EquityTables
import HandEvaluator

""" This class represents the current state of the bot
    and all of the information that the bot is aware of
"""

class BotState:
    def __init__(self):
        #current hand state
        self.handState = "" # will be 'preflop','flop','discard','turn','river'
        
        #equity calculation stuff
        self.preFlopTable = EquityTables.MakePreFlopTable()

        #bot global variables
        self.bank = 0
        self.oppBank = 0
        self.timeBank = 0.0


        #match variables:
        self.name = ''
        self.oppName = ''
        self.stackSize = 0
        self.bb = 0
        self.numHands = 0

        #current hand variables 
        self.dealer = False
        self.handId = 0
        self.boardCards = []
        self.lastActions = []
        self.legalActions = []
        self.hand = []
        self.discardedCard = ''
        self.pot = 0
        self.stake = 0
        #... fill in more as we figure out how dis shit works

        #Set to determine which round the bot goes all in, 0 for preflop to 3 for river
        self.allInRound = 0
        return

    # Given a parsed input, update the bot's state and information 
    def update(self, inp):
        inSplit = inp.split(' ')
        if inSplit[0] == 'NEWGAME': # initialize game parameters 
            self.name = inSplit[1]
            self.oppName = inSplit[2]
            self.stackSize = int(inSplit[3])
            self.bb = int(inSplit[4])
            self.numHands = int(inSplit[5])
            self.timeBank = float(inSplit[6])
            """
            print "name is " + self.name
            print "oppname is " + self.oppName
            print "stacksize is " + str(self.stackSize)
            print "big blind is " + str(self.bb)
            print "numHands is " + str(self.numHands)
            print "timebank is " + str(self.timeBank)
            print ""
            print ""
            """
 

        elif inSplit[0] == 'NEWHAND': # reset hand-specific parameters
            self.handState = 'preflop'
            self.handId = int(inSplit[1])
            self.dealer = bool(inSplit[2])
            self.hand = [inSplit[3], inSplit[4], inSplit[5]]
            self.discardedCard = ''
            self.bank =  int(inSplit[6])
            self.oppBank = int(inSplit[7])
            self.timeBank = float(inSplit[8])
            self.legalActions = []
            self.lastActions = []
            """
            print "handid is " + str(self.handId)
            print "dealer is " + str(self.dealer)
            print "hand is " + str(self.hand)
            print "bank is " + str(self.bank)
            print "oppBank is " + str(self.oppBank)
            print "timebank is " + str(self.timeBank)
            print ""
            print ""
            """


        elif inSplit[0] == 'GETACTION': # update current board and stuff
            self.pot = int(inSplit[1])
            numBoardCards = int(inSplit[2])
            endBoardCards = 2 + numBoardCards
            self.boardCards = inSplit[3:endBoardCards + 1]
            if len(self.boardCards)== 3:
                self.handState = 'flop'
            elif len(self.boardCards) == 4:
                self.handState = 'turn'
            elif len(self.boardCards) == 5:
                self.handState = 'river'
                    
            numLastActions = int(inSplit[endBoardCards + 1])
            endLastActions = endBoardCards + 1 + numLastActions
            self.lastActions = [act.split(':') for act in inSplit[endBoardCards + 2:endLastActions + 1]]
            
            numLegalActions = int(inSplit[endLastActions + 1])
            endLegalActions = endLastActions + 1 + numLegalActions
            self.legalActions = [act.split(':') for act in inSplit[endLastActions + 2:endLegalActions + 1]]

            self.timebank = float(inSplit[-1])
            
            if self.legalActions[0][0] == 'DISCARD':
                self.handState = 'discard'
                        
            """
            print "pot is " + str(self.pot)
            print "board is is " + str(self.boardCards)
            print "last actons isis " + str(self.lastActions)
            print "legal Actions is " + str(self.legalActions)
            print ""
            print ""
            """

        elif inSplit[0] == 'HANDOVER':
            self.bank = int(inSplit[1])
            self.oppBank = int(inSplit[2])
            numBoardCards = int(inSplit[3])
            endBoardCards = 3 + numBoardCards
            self.boardCards = inSplit[4:endBoardCards]
            numLastActions = int(inSplit[endBoardCards + 1])
            endLastActions = endBoardCards + 2 + numLastActions
            self.lastActions = [act.split(':') for act in inSplit[endBoardCards + 2:endLastActions]]
            self.timeBank = float(inSplit[-1])
            """
            print "bank " + str(self.bank)
            print "oppbank is " + str(self.oppBank)
            print "boardCards is " + str(self.boardCards)
            print "numlast actions is " + str(self.numLastActions)
            print "last asctions is  " + str(self.lastActions)
            print "timebank is " + str(self.timeBank)
            print ""
            print ""
            """
            
        else:
            pass
        return

    def decideAction(self):
        action = 'CHECK\n'
        if self.handState == 'preflop':
            if self.allInRound == 0:
                for possibleAction in self.legalActions:
                    if possibleAction[0] == 'RAISE':
                        action = 'RAISE:'+possibleAction[2]+'\n'
                        break
                    elif possibleAction[0] == 'BET':
                        action = 'BET:'+possibleAction[2]+'\n'
                        break
                if ['CALL'] in self.legalActions and action == 'CHECK\n':
                    action = 'CALL\n'
            else:
                if ['CALL'] in self.legalActions:
                    action = 'CALL\n'
                else:
                    pass
        elif self.handState == 'flop':
            if self.allInRound == 1:
                for possibleAction in self.legalActions:
                    if possibleAction[0] == 'RAISE':
                        action = 'RAISE:'+possibleAction[2]+'\n'
                        break
                    elif possibleAction[0] == 'BET':
                        action = 'BET:'+possibleAction[2]+'\n'
                        break
                if ['CALL'] in self.legalActions and action == 'CHECK\n':
                    action = 'CALL\n'
            else:
                if ['CALL'] in self.legalActions:
                    action = 'CALL\n'
                else:
                    pass
        elif self.handState == 'discard':
            pass
        elif self.handState == 'turn':
            if self.allInRound == 2:
                for possibleAction in self.legalActions:
                    if possibleAction[0] == 'RAISE':
                        action = 'RAISE:'+possibleAction[2]+'\n'
                        break
                    elif possibleAction[0] == 'BET':
                        action = 'BET:'+possibleAction[2]+'\n'
                        break
                if ['CALL'] in self.legalActions and action == 'CHECK\n':
                    action = 'CALL\n'
            else:
                if ['CALL'] in self.legalActions:
                    action = 'CALL\n'
                else:
                    pass
        elif self.handState == 'river':
            if self.allInRound == 3:
                for possibleAction in self.legalActions:
                    if possibleAction[0] == 'RAISE':
                        action = 'RAISE:'+possibleAction[2]+'\n'
                        break
                    elif possibleAction[0] == 'BET':
                        action = 'BET:'+possibleAction[2]+'\n'
                        break
                if ['CALL'] in self.legalActions and action == 'CHECK\n':
                    action = 'CALL\n'
            else:
                if ['CALL'] in self.legalActions:
                    action = 'CALL\n'
                else:
                    pass
        else:
            # should not get here
            pass
        return action
