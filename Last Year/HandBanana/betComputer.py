import random

def computePreFlopBet(potEquity, amtToCall, potSize, position, bigBlind, bankRollState, handID, numHands):
    lastDitch = False

    potOdds = float(amtToCall) / (amtToCall + potSize)
    if potOdds > potEquity:
        bet = -1
    else:
        bet = int((potEquity * potSize) / (1 - .999*potEquity))

#    if abs(bankRollState[2]) > 75 * (numHands - handID + 1) and bankRollState[2] < 0:
#        if potSize < 75:
#            bet = random.randrange(25, 50)
#        else:
#            bet = amtToCall
#        lastDitch = True
    return bet, lastDitch




def computePreFlopAction(bet, position, amtToCall, smallBlind, bigBlind, minimumRaise, canCheck,stackSize, isBluffing, equity, previousBet, bankRollState, lastDitch):
    isBluffing = False
    action = 0
    cost = 0
    if bet == -1:
        if canCheck:
            action = 'CHECK\n'
            cost = 0
        else:
            if not isBluffing and amtToCall >= stackSize*0.9 and equity > 0.60:
                action = 'CALL\n'
                cost = amtToCall
            elif isBluffing:
                action = 'SWITCH HANDS'
                cost = 0
            else:
                action = 'FOLD\n'
                cost = 0
    elif bet == amtToCall:
        if amtToCall == 0:
            action = 'CHECK\n'
            cost = 0
        else:
            action = 'CALL\n'
            cost = amtToCall
    else:
        if position == 0:
            value = bet
        elif position == 1:
            value = bet + smallBlind
        else:
            value = bet + bigBlind
        if not isBluffing:

            #Should Involve Equity In This Case To Determine If We Should Fold
            if value < minimumRaise or amtToCall == stackSize - previousBet:
                action = 'CALL\n'
                cost = amtToCall
            else:
                #Equity threshold of willing to go all in 0.6
                #Below that we'll have a function from 0.33 to 0.6 to find our
                #Max raise value, but if advantageous we'll still call
                maxRaise = computeMaxRaise(equity,stackSize)
                if (value >= maxRaise and not lastDitch):
                    action = 'CALL\n'
                    cost = amtToCall

                else:
                    if value > stackSize:
                        value = stackSize
                    action = 'RAISE:' + str(value) + '\n'
                    cost = value - previousBet
        else:
            if amtToCall > value/2 or value < minimumRaise or amtToCall == stackSize - previousBet:
                action = 'SWITCH HANDS'
                cost = 0
            else:
                if value > stackSize:
                    value = stackSize

                
                action = 'RAISE:' + str(value) + '\n'
                cost = value - previousBet

    #if position == 0 and equity < .5:
    #    action = 'FOLD\n'
    #    cost = 0
    #elif position == 1 and equity < .4:
    #    action = 'FOLD\n'
    #    cost = 0

    return action, cost




def computePostFlopBet(potEquity, amtToCall, potSize, newDealPotSize, position):
    #Will impliment position later
    pot = computeWeightedPot(potSize, newDealPotSize, 1)

    potOdds = float(amtToCall) / (amtToCall + pot)

    if potOdds > potEquity:
        bet = -1
    else:
        bet = int((potEquity * pot) / (1 - .999*potEquity))

    

    return bet

def computePostFlopAction(bet, position, amtToCall, minimumRaise, canCheck, minBet,stackSize, isBluffing, equity, previousBet, isLeftIn, isRightIn, lastOpponentBet, currentPotSize, boardLength, bankRollState):
    action = 0
    cost = 0
    if bet == -1:
        if canCheck:
            action = 'CHECK\n'
            cost = 0
        else:
            action = 'FOLD\n'
            cost = 0
    elif bet == amtToCall:
        if amtToCall == 0:
            action = 'CHECK\n'
            cost = 0
        else:
            action = 'CALL\n'
            cost = amtToCall
    else:
        value = bet
        lowerBound = 0
        upperBound = 0
        if isLeftIn and isRightIn:
            lowerBound = 0.33
            upperBound = 0.6
        else:
            lowerBound = 0.5
            upperBound = 0.7
            
        if equity < lowerBound and not isBluffing:
            value = 0
        elif equity < upperBound and not isBluffing:
            value = int((equity - lowerBound)/(upperBound - lowerBound) * value)

        if canCheck:
            if value < minBet:
                action = 'CHECK\n'
                cost = 0
            else:
                if value > stackSize:
                    value = stackSize

                #Changes here, maybe optimize with simulations
                if (boardLength == 3 or boardLength == 4) and ((position == 2 and isRightIn) or (position == 0)):
                    if int(value*0.33) > minBet:
                        value = int(value*0.33)
                elif boardLength == 5 and bankRollState[0] == 'BEHIND' and equity > .55:
                    value = stackSize
                    
                action = 'BET:' + str(value) + '\n'
                cost = value
        else:
            opponentEquity = float(lastOpponentBet)/float(currentPotSize)

            if not isBluffing:
                    
                if equity < opponentEquity*0.9:
                    action = 'FOLD\n'
                    cost = 0
                elif equity < opponentEquity*1.1:
                    action = 'CALL\n'
                    cost = amtToCall
                else:
                    if value < minimumRaise or amtToCall == stackSize - previousBet:
                        action = 'CALL\n'
                        cost = amtToCall
                    else:
                        if value > stackSize:
                            value = stackSize
                        if (boardLength == 3 or boardLength == 4) and amtToCall < value/5:
                            if int(value*0.33) > minimumRaise:
                                value = int(value*0.33)
                        elif boardLength == 5 and bankRollState[0] == 'BEHIND' and equity > .55:
                            value = stackSize

                        action = 'RAISE:' + str(value) + '\n'
                        cost = value - previousBet
            else:
                if amtToCall > value/2 or value < minimumRaise or amtToCall == stackSize - previousBet:
                    action = 'SWITCH HANDS'
                    cost = 0
                else:
                    if value > stackSize:
                        value = stackSize
                    action = 'RAISE:' + str(value) + '\n'
                    cost = value - previousBet

    return action, cost




def induceBetVariance(bet):
    rand = random.gauss(0, .25/3)
    rand = rand + 1
    rand = bet * rand
    if rand > 1.25 * bet:

        return int(round(bet * 1.25))
    elif rand < .75 * bet:
        return int(round(bet * .75))
    return int(round(rand))


def computeMaxRaise(equity,stackSize):
    if (equity >= 0.7):
        return stackSize
    elif (equity >= 0.33):
        return stackSize*((equity-0.33)/(0.7-0.33))
    else:
        return 0




def computeWeightedPot(potSize, newDealPotSize, scale):
    return potSize*scale + newDealPotSize*(1 - scale)











    
