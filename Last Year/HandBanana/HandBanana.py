#Turn off bluffing if we have a good hand#


import socket
import sys
import customPoker
import betComputer
from pokereval import PokerEval
import random
from bluffer import Bluffer
from OpponentTracker import OpponentTracker

POKER = PokerEval()
preFlopTable2 = customPoker.makePreFlopTable2()
preFlopTable3 = customPoker.makePreFlopTable3()


#Global Variables such as cards, bank, ....

#New Game

state = 0
opponents = {}
leftOp = ''
rightOp = ''

leftOpAverageWin = 0
rightOpAverageWin = 0


numHands = 0
bank = 0
bigBlind = 0
smallBlind = 0
leftBank = 0
rightBank = 0
timeBank = 0
stackSize = 0

#May not be nessesary...

amtToCall = 0
previousBet = 0

minimumRaise = 0
canCheck = False

#Zero if cannot bet, otherwise assigned to minimum Bet Value
minBet = 0

#New Hand

handID = 0
position = 0
hand = []
boardCards = []

potSize = 0
runningPot = 0
newDealPot = 0
lastOpBet = 0

currentStakePreFlop = 0
currentStakePostFlop = 0
numberPostFlopHands = 0
totalWinPreFlop = 0
totalWinPostFlop = 0
totalLossPreFlop = 0
totalLossPostFlop = 0
finalPreFlopPotSize = 0
madePastFlop = False
numberOfWins = 0
numberOfPostFlopWins = 0

averageWinPreFlop = 0
averageWinPostFlop = 0
averageLossPreFlop = 0
averageLossPostFlop = 0

STACK = 0

smallPotPlayerRight = False
smallPotPlayerLeft = False

bankRollState = 'NEUTRAL', 'DICKS', 0
#Player State

leftPlayerIn = True
rightPlayerIn = True

newLeft = True
newRight = True

#Actions

previousActions = []
legalActions = []


#Bluffer
bluffer = Bluffer()


#Parser
################################################################################
def parser(string):
    global state, leftOp, rightOp, leftPlayerIn, rightPlayerIn, minBet, bluffer, averageWinPreFlop, averageWinPostFlop, averageLossPreFlop, opponents
    global numHands, bank, leftBank, rightBank, minimumRaise, canCheck, STACK, runningPot, newDealPot, averageLossPostFlop, smallPotPlayerLeft, newLeft, newRight
    global bigBlind, smallBlind, timeBank, position, hand, handID, stackSize, previousBet, lastOpBet, numberOfWins,numberOfPostFlopWins, smallPotPlayerRight
    global boardCards, previousActions, legalActions, amtToCall, potSize, currentStakePreFlop, currentStakePostFlop, numberPostFlopHands, leftOpAverageWin
    global totalWinPreFlop, totalWinPostFlop, totalLossPreFlop, totalLossPostFlop, finalPreFlopPotSize, madePastFlop, bankRollState, rightOpAverageWin
    
    stringSplit = string.split(' ')
    
    if stringSplit[0] == 'NEWGAME':
        
        averageWinPreFlop = 0
        averageWinPostFlop = 0
        averageLossPreFlop = 0
        averageLossPostFlop = 0
        
        numberOfWins = 0
        numberOfPostFlopWins = 0
        bank = 0
        leftBank = 0
        rightBank = 0
        state = stringSplit[0]
        numHands = int(stringSplit[4])
        leftOp = stringSplit[2]
        rightOp = stringSplit[3]
        if leftOp not in opponents:
            opponents[leftOp] = [0,0]
            newLeft = True
        else:
            newLeft = False
        if rightOp not in opponents:
            opponents[rightOp] = [0,0]
            newRight = True
        else:
            newRight = False
        
        STACK = int(stringSplit[5])
        
        bigBlind = int(stringSplit[6])
        smallBlind = int(stringSplit[7])
        
        timeBank = float(stringSplit[8])
        leftOpAverageWin = 0
        rightOpAverageWin = 0
        numberPostFlopHands = 0
        totalWinPreFlop = 0
        totalWinPostFlop = 0
        totalLossPreFlop = 0
        totalLossPostFlop = 0
        bankRollState = 'NEUTRAL', 'DEATH TO CHEESEBOT!!!!', 0

        bluffer = Bluffer()
        
    elif stringSplit[0] == 'NEWHAND':
        madePastFlop = False
        state = stringSplit[0]
        previousBet = 0
        bluffer.nextRound()
        finalPreFlopPotSize = 0
        handID = int(stringSplit[1])
        position = int(stringSplit[2])
        hand = [stringSplit[3], stringSplit[4]]
        stackSize = STACK

        runningPot = 0
        #bank += int(stringSplit[5])
        #leftBank += int(stringSplit[6])
        #rightBank += int(stringSplit[7])
        
        timeBank = float(stringSplit[8])

        leftPlayerIn,rightPlayerIn = True,True

        #May need to fix this
        
        if position == 0:
            currentStakePreFlop = 0
            currentStakePostFlop = 0
            amtToCall = bigBlind
            previousBet = 0
        elif position == 1:
            currentStakePreFlop = smallBlind
            currentStakePostFlop = 0
            amtToCall = bigBlind - smallBlind
            previousBet = smallBlind
        else:
            currentStakePreFlop = bigBlind
            currentStakePostFlop = 0
            amtToCall = 0
            previousBet = bigBlind
            


    elif stringSplit[0] == 'GETACTION':
        minBet = 0
        #I believe this should be...
        minimumRaise = 0
        canCheck = False
        offset = 0
        state = stringSplit[0]
        potSize = int(stringSplit[1])
        if stringSplit[2] == '0':
            offset -= 1
            boardCards = []
        else:
            boardCards = stringSplit[3].split(',')
        if stringSplit[4 + offset] == '0':
            offset -= 1
            actions = []
        else:
            actions = stringSplit[5 + offset].split(',')
        if stringSplit[6 + offset] == '0':
            offset -= 1
            legal = []
        else:
            legal = stringSplit[7 + offset].split(',')
        timeBank = stringSplit[8 + offset]


        previousActions = [action.split(':') for action in actions]
        legalActions = [action.split(':') for action in legal]
        
        
        maxBet = 0

        hasDealt = False
        postDealBets = 0
        for action in previousActions:
            if action[0] == 'FOLD':
                if action[1] == leftOp:
                    leftPlayerIn = False
                elif action[1] == rightOp:
                    rightPlayerIn = False
                    
            elif action[0] == 'RAISE' or action[0] == 'BET':
                if int(action[2]) > maxBet:
                    maxBet = int(action[2])
                if hasDealt:
                    postDealBets += int(action[2])
            elif action[0] == 'CALL' and hasDealt:
                postDealBets *= 2
                
            elif action[0] == 'DEAL' and len(boardCards) != 0:
                amtToCall = 0
                stackSize -= previousBet
                previousBet = 0
                maxBet = 0
                hasDealt = True
                runningPot = potSize
                if len(boardCards) == 3:
                    madePastFlop = True
                    numberPostFlopHands += 1 


                    if previousActions[-1][0] == 'DEAL':
                        finalPreFlopPotSize = potSize
                    elif previousActions[-2][0] == 'DEAL':
                        if previousActions[-1][0] == 'CHECK' or previousActions[-1][0] == 'FOLD':
                            finalPreFlopPotSize = potSize
                        else:
                            finalPreFlopPotSize = potSize - int(previousActions[-1][-1])
                    elif previousActions[-3][0] == 'DEAL':
                        diff = 0
                        if previousActions[-2][0] == 'CHECK' or previousActions[-2][0] == 'FOLD':
                            if previousActions[-1][0] == 'CHECK' or previousActions[-1][0] == 'FOLD':
                                finalPreFlopPotSize = potSize
                            else:
                                finalPreFlopPotSize = potSize - int(previousActions[-1][-1])
                        else:
                            diff = int(previousActions[-2][-1])
                            if previousActions[-1][0] == 'CALL':
                                diff *= 2
                            elif previousActions[-1][0] == 'RAISE':
                                diff += int(previousActions[-1][-1])
                        finalPreFlopPotSize  = potSize - diff
                
        if previousActions[-1][0] == 'BET' or previousActions[-1][0] == 'RAISE':
            lastOpBet = int(previousActions[-1][2])
        elif previousActions[-1][0] == 'CALL' or previousActions[-1][0] == 'FOLD':
            if previousActions[-2][0] == 'BET' or previousActions[-2][0] == 'RAISE':
                lastOpBet = int(previousActions[-2][2])
            else:
                lastOpBet = 0
        else:
            lastOpBet = 0
            

        if maxBet != 0:           
            amtToCall = maxBet - previousBet
            
        for action in legalActions:
            if action[0] == 'RAISE':
                minimumRaise = int(action[1])
            elif action[0] == 'CHECK':
                canCheck = True
            elif action[0] == 'BET':
                minBet = int(action[1])

                    
        newDealPot = potSize - runningPot + postDealBets
                

    else:
        offset = 0
        state = stringSplit[0]
        if bank < int(stringSplit[1]):
            if madePastFlop:
                totalWinPreFlop += finalPreFlopPotSize - currentStakePreFlop
                totalWinPostFlop += (int(stringSplit[1]) - bank) - (finalPreFlopPotSize - currentStakePreFlop)
                numberOfWins += 1
                numberOfPostFlopWins += 1
            else:
                win = int(stringSplit[1]) - bank
                totalWinPreFlop += win
                numberOfWins += 1
        else:
            if madePastFlop:
                totalLossPreFlop += currentStakePreFlop
                totalLossPostFlop += currentStakePostFlop
            else:
                loss = bank - int(stringSplit[1])
                totalLossPreFlop += loss
        
        bank = int(stringSplit[1])
        leftBank = int(stringSplit[2])
        rightBank = int(stringSplit[3])
        if stringSplit[4] == '0':
            offset -= 1
            previousActions = []
        else:
            previousActions = stringSplit[5].split(',')
        timeBank = stringSplit[6 + offset]

        previousActions = [action.split(':') for action in previousActions]

        if numberOfWins == 0:
            averageWinPreFlop = 0
        else:
            averageWinPreFlop = float(totalWinPreFlop)/numberOfWins
        if numberOfPostFlopWins == 0:
            averageWinPostFlop = 0
        else:
            averageWinPostFlop = float(totalWinPostFlop)/numberOfPostFlopWins
        if handID == numberOfWins:
            averageLossPreFlop = 0
        else:
            averageLossPreFlop = float(totalLossPreFlop)/(handID - numberOfWins)
        if numberPostFlopHands == numberOfPostFlopWins:
            averageLossPostFlop = 0
        else:
            averageLossPostFlop = float(totalLossPostFlop)/(numberPostFlopHands - numberOfPostFlopWins)

        OpBank = max(leftBank,rightBank)
        if bank < OpBank + 1000 and bank > OpBank - 1000:
            bankRollState = 'NEUTRAL', 'DEATH TO CHEESEBOT!!!!', bank - OpBank
        elif bank >= OpBank + 1000:
            if totalWinPostFlop > totalWinPreFlop:
                bankRollState = 'AHEAD', 'POST', bank - OpBank
            else:
                bankRollState = 'AHEAD', 'PRE', bank - OpBank
        else:
            if totalLossPostFlop > totalLossPreFlop:
                bankRollState = 'BEHIND', 'POST', bank - OpBank
            else:
                bankRollState = 'BEHIND', 'PRE', bank - OpBank


        for action in previousActions:
            if action[0] == 'WIN':
                if action[1] == leftOp:
                    
                    opponents[leftOp][0] += 1
                    opponents[leftOp][1] += int(action[2])
                
                    leftOpAverageWin = float(opponents[leftOp][1])/opponents[leftOp][0]
                elif action[1] == rightOp:
                    
                    opponents[rightOp][0] += 1
                    opponents[rightOp][1] += int(action[2])
                    
                    rightOpAverageWin = float(opponents[rightOp][1])/opponents[rightOp][0]
        if (float(handID)/numHands > .12 and newLeft) or not newLeft:
            if leftOpAverageWin < 50:
                smallPotPlayerLeft = True
            else:
                smallPotPlayerLeft = False
                
        if (float(handID)/numHands > .12 and newRight) or not newRight:
            if rightOpAverageWin < 50:
                smallPotPlayerRight = True
            else:
                smallPotPlayerRight = False


        
        if bluffer.wait == 0:
            bluffer.reset()
        
################################################################################
        
#Finds Equity

def getPreFlopEquity():
    global preFlopTable3, preFlopTable2, leftPlayerIn, rightPlayerIn, totalWinPreFlop, totalLossPreFlop
    if leftPlayerIn and rightPlayerIn:

        
        equity = preFlopTable3[customPoker.getPreflopString(hand)]

        if totalLossPreFlop > totalWinPreFlop:
            equity *= .9
        return equity
    else:

        
        equity = preFlopTable2[customPoker.getPreflopString(hand)]
        if totalLossPreFlop > totalWinPreFlop:
            equity *= .9

        
        return equity

################################################################################















    








if __name__ == "__main__":
    # port number specified by the engine to connect to.
    port = int(sys.argv[1])
    # connect the socket to the engine
    s = socket.create_connection(('localhost', int(sys.argv[1])))
    # Get a file-object for reading packets from the socket.
    # Using this ensures that you get exactly one packet per read.
    f_in = s.makefile()
    while 1:
        # block until the engine sends us a packet
        data = f_in.readline()
        # if we receive a null return, then the connection is dead
        if not data:

            break
        # Here is where you should implement code to parse the packets from
        # the engine and act on it.
        

        
        # When appropriate, reply to the engine with a legal action.
        # The engine will ignore all spurious packets you send.
        # The engine will also check/fold for you if you return an
        # illegal action.
        # When sending responses, you need to have a newline character (\n) or
        # carriage return (\r), or else your bot will hang!
        
        #Update Global Variables
        parser(data)
        
        action = 'CALL\n'
        
        if state == 'GETACTION':
            
            if len(boardCards) == 0:
                #if bluffer.isBluff(bankRollState, numHands, handID):
                #    equity = bluffer.bluffHandPercentPreFlop()
                #else:
                equity = getPreFlopEquity()
                bet = betComputer.computePreFlopBet(equity, amtToCall, potSize, position, bigBlind, bankRollState, handID, numHands)[0]
                lastDitch = betComputer.computePreFlopBet(equity, amtToCall, potSize, position, bigBlind, bankRollState, handID, numHands)[1]
                bet = betComputer.induceBetVariance(bet)
                action = betComputer.computePreFlopAction(bet, position, amtToCall, smallBlind, bigBlind, minimumRaise, canCheck, stackSize, bluffer.isBluff(bankRollState, numHands, handID), equity, previousBet, bankRollState, lastDitch)
                if action[0] == 'SWITCH HANDS':

                    equity = getPreFlopEquity()
                    bet = betComputer.computePreFlopBet(equity, amtToCall, potSize, position, bigBlind)
                    bet = betComputer.induceBetVariance(bet)
                    action = betComputer.computePreFlopAction(bet, position, amtToCall, smallBlind, bigBlind, minimumRaise, canCheck, stackSize, False, equity, previousBet, bankRollState)


                currentStakePreFlop += action[1]


            elif len(boardCards) == 3:
                if bluffer.isBluff(bankRollState, numHands, handID):
                    probOfWin = bluffer.bluffHandPercent(boardCards,POKER,leftPlayerIn,rightPlayerIn)
                else:
                    probOfWin = customPoker.probOfWin(POKER,hand,boardCards, leftPlayerIn, rightPlayerIn, totalWinPostFlop - totalLossPostFlop)
                    if leftPlayerIn and rightPlayerIn and smallPotPlayerLeft and smallPotPlayerRight:
                        probOfWin *= .9
                    elif leftPlayerIn and not rightPlayerIn and smallPotPlayerLeft:
                        probOfWin *= .9
                    elif rightPlayerIn and not leftPlayerIn and smallPotPlayerRight:
                        probOfWin *= .9
                bet = betComputer.computePostFlopBet(probOfWin, amtToCall, potSize, newDealPot, position)
                bet = betComputer.induceBetVariance(bet)
                action = betComputer.computePostFlopAction(bet,position,amtToCall,minimumRaise,canCheck,minBet,stackSize, bluffer.isBluff(bankRollState, numHands, handID), probOfWin, previousBet, leftPlayerIn, rightPlayerIn,lastOpBet, potSize, len(boardCards), bankRollState)
                if action[0] == 'SWITCH HANDS':

                    probOfWin = customPoker.probOfWin(POKER,hand,boardCards, leftPlayerIn, rightPlayerIn, totalWinPostFlop - totalLossPostFlop)
                    bet = betComputer.computePostFlopBet(probOfWin, amtToCall, potSize, newDealPot, position)
                    bet = betComputer.induceBetVariance(bet)
                    action = betComputer.computePostFlopAction(bet, position, amtToCall, minimumRaise, canCheck, minBet, stackSize, False, probOfWin, previousBet, leftPlayerIn, rightPlayerIn,lastOpBet, potSize, len(boardCards), bankRollState)

                currentStakePostFlop += action[1] 

                
            elif len(boardCards) == 4:
                if bluffer.isBluff(bankRollState, numHands, handID):
                    probOfWin = bluffer.bluffHandPercent(boardCards,POKER,leftPlayerIn,rightPlayerIn)
                else:
                    probOfWin = customPoker.probOfWin(POKER,hand,boardCards, leftPlayerIn, rightPlayerIn, totalWinPostFlop - totalLossPostFlop)
                bet = betComputer.computePostFlopBet(probOfWin, amtToCall, potSize, newDealPot, position)
                bet = betComputer.induceBetVariance(bet)
                action = betComputer.computePostFlopAction(bet,position,amtToCall,minimumRaise,canCheck,minBet,stackSize, bluffer.isBluff(bankRollState, numHands, handID), probOfWin, previousBet, leftPlayerIn, rightPlayerIn,lastOpBet, potSize, len(boardCards), bankRollState)
                if action[0] == 'SWITCH HANDS':

                    probOfWin = customPoker.probOfWin(POKER,hand,boardCards, leftPlayerIn, rightPlayerIn, totalWinPostFlop - totalLossPostFlop)
                    bet = betComputer.computePostFlopBet(probOfWin, amtToCall, potSize, newDealPot, position)
                    bet = betComputer.induceBetVariance(bet)
                    action = betComputer.computePostFlopAction(bet, position, amtToCall, minimumRaise, canCheck, minBet, stackSize, False, probOfWin, previousBet, leftPlayerIn, rightPlayerIn,lastOpBet, potSize, len(boardCards), bankRollState)


                currentStakePostFlop += action[1]
                
            elif len(boardCards) == 5:
                if bluffer.isBluff(bankRollState, numHands, handID):
                    probOfWin = bluffer.bluffHandPercent(boardCards,POKER,leftPlayerIn,rightPlayerIn)
                else:
                    probOfWin = customPoker.probOfWin(POKER,hand,boardCards, leftPlayerIn, rightPlayerIn, totalWinPostFlop - totalLossPostFlop)
                bet = betComputer.computePostFlopBet(probOfWin, amtToCall, potSize, newDealPot, position)
                bet = betComputer.induceBetVariance(bet)
                action = betComputer.computePostFlopAction(bet,position,amtToCall,minimumRaise,canCheck,minBet,stackSize, bluffer.isBluff(bankRollState, numHands, handID), probOfWin, previousBet, leftPlayerIn, rightPlayerIn,lastOpBet, potSize, len(boardCards), bankRollState)
                if action[0] == 'SWITCH HANDS':

                    probOfWin = customPoker.probOfWin(POKER,hand,boardCards, leftPlayerIn, rightPlayerIn, totalWinPostFlop - totalLossPostFlop)
                    bet = betComputer.computePostFlopBet(probOfWin, amtToCall, potSize, newDealPot, position)
                    bet = betComputer.induceBetVariance(bet)
                    action = betComputer.computePostFlopAction(bet, position, amtToCall, minimumRaise, canCheck, minBet, stackSize, False, probOfWin, previousBet, leftPlayerIn, rightPlayerIn,lastOpBet, potSize, len(boardCards), bankRollState)


                currentStakePostFlop += action[1]

            previousBet += action[1] #Make sure affected by action   


            s.send(action[0])

    s.close()



