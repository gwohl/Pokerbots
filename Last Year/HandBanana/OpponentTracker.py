class OpponentTracker:
    def __init__(self, opponent):
        self.state = 'PREFLOP'
        
        self.opponent = opponent
        self.currentHandNumber = 1
        
        self.handsFoldedPreFlop = 0
        self.handsFoldedPreFlopRatio = 0
        
        self.totalPostFlopHands = 0
        self.handsFoldedPostFlop = 0
        self.handsFoldedPostFlopRatio = 0
        
        self.totalTurnHands = 0
        self.handsFoldedTurn = 0
        self.handsFoldedTurnRatio = 0

        self.totalRiverHands = 0
        self.handsFoldedRiver = 0
        self.handsFoldedRiverRatio = 0

        
        self.averageBetFoldedOn = [0,0]
        self.bluffPercent = [0,0]

    def update(self, previousActions, handID):
        self.currentHandNumber = handID
        for action in previousActions:
            if action[0] == 'DEAL':
                self.state = action[1]
            elif action[0] == 'FOLD' and action[1] == self.opponent:
                if self.state == 'PREFLOP':
                    self.handsFoldedPreFlop += 1
                    self.handsFoldedPreFlopRatio = float(self.handsFoldedPreFlop)/self.currentHandNumber
                elif self.state == 'FLOP':
                    self.totalPostFlopHands = self.currentHandNumber - self.handsFoldedPreFlop
                    self.handsFoldedPostFlop += 1
                    self.handsFoldedPostFlopRatio = float(self.handsFoldedPostFlop)/self.totalPostFlopHands
                elif self.state == 'TURN':
                    self.totalTurnHands = self.currentHandNumber - self.handsFoldedPostFlop - self.handsFoldedPreFlop
                    self.handsFoldedTurn += 1
                    self.handsFoldedTurnRatio = float(self.handsFoldedTurn)/self.totalTurnHands
                elif self.state == 'RIVER':
                    self.totalRiverHands = self.currentHandNumber - self.handsFoldedPostFlop - self.handsFoldedPreFlop - self.handsFoldedTurn
                    self.handsFoldedRiver += 1
                    self.handsFoldedRiverRatio = float(self.handsFoldedRiver)/self.totalRiverHands
                    
                
                
                

        
