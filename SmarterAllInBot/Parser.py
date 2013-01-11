import Action
class ParsedInput:
    def __init__(self, inp):
        inSplit = inp.split(' ')
        self.state = inSplit[0]
        if self.state == 'NEWGAME': #NEWGAME packet
            self.yourName = inSplit[1]
            self.oppName = inSplit[2]
            self.stackSize = int(inSplit[3])
            self.bb = int(inSplit[4])
            self.numHands = int(inSplit[5])
            self.timeBank = float(inSplit[6])

        elif self.state == 'KEYVALUE': #KEYVALUE packet
            self.key = inSplit[1]
            self.value = inSplit[2]

        elif self.state == 'REQUESTKEYVALUES':
            self.bytesLeft = inSplit[1]

        elif self.state == 'NEWHAND':
            self.handId = int(inSplit[1])
            self.button = bool(inSplit[2])
            self.hand = [inSplit[3], inSplit[4], inSplit[5]]
            self.yourBank = int(inSplit[6])
            self.oppBank = int(inSplit[7])
            self.timeBank = float(inSplit[8])

        elif self.state == 'GETACTION':
            self.potSize = int(inSplit[1])
            self.numBoardCards = int(inSplit[2])
            endBoardCards = 2 + self.numBoardCards
            self.boardCards = inSplit[3:endBoardCards + 1]
            self.numLastActions = int(inSplit[endBoardCards + 1])
            endLastActions = endBoardCards + 1 + self.numLastActions
            
            self.lastActions = inSplit[endBoardCards + 2:endLastActions + 1]
                        
            self.numLegalActions = int(inSplit[endLastActions + 1])
            endLegalActions = endLastActions + 1 + self.numLegalActions
            
            self.legalActions = inSplit[endLastActions + 2:endLegalActions + 1]
 
            
            self.timebank = float(inSplit[-1])


        elif self.state == 'HANDOVER':
            self.yourBank = int(inSplit[1])
            self.oppBank = int(inSplit[2])
            self.numBoardCards = int(inSplit[3])
            endBoardCards = 3 + self.numBoardCards
            self.boardCards = inSplit[4:endBoardCards]
            self.numLastActions = int(inSplit[endBoardCards + 1])
            endLastActions = endBoardCards + 1 + self.numLastActions
            
            self.lastActions = inSplit[endBoardCards + 2:endLastActions]
        
            self.timeBank = float(inSplit[-1])

        else:
            pass #should not get here
        return 



