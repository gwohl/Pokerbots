class Action:
    def __init__(self, inString):
        s = inString.split(':')
        t = s[0]
        if t == 'BET':
            self.type = 'bet'
            self.minBet = int(s[1])
            self.maxBet = int(s[2])
        elif t == 'CALL':
            self.type = 'call'
        elif t == 'CHECK':
            self.type = 'check'
        elif t == 'DISCARD':
            self.type = 'discard'
        elif t == 'FOLD':
            self.type = 'fold'
        elif t == 'RAISE':
            self.type = 'raise'
            self.minRaise = int(s[1])
            self.maxRaise = int(s[2])
        else:
            pass #should not get here
        return 
class PerformedAction:
    def __init__(self, inString):
        s = inString.split(':')
        t = s[0]
        if t == 'BET':
            self.type = 'bet'
            self.amount = int(s[1])
            self.actor = s[2]
        elif t == 'CALL':
            self.type = 'call'
            self.actor = s[1]
        elif t == 'CHECK':
            self.type = 'check'
            self.actor = s[1]
        elif t == 'DEAL':
            self.type = 'deal'
            self.street = s[1]
        elif t == 'DISCARD':
            self.type = 'discard'
            self.card = s[1]
        elif t == 'FOLD':
            self.type = 'fold'
            self.actor = s[1]
        elif t == 'POST':
            self.type = 'post'
            self.amount = int(s[1])
            self.actor = s[2]
        elif t == 'RAISE':
            self.type = 'raise'
            self.amount = int(s[1])
            self.actor = s[2]
        elif t == 'REFUND':
            self.type = 'refund'
            self.amount = int(s[1])
            self.actor = s[2]
        elif t == 'SHOW':
            self.type = 'show'
            self.hand = [s[1],s[2]]
            self.actor = s[3]
        elif t == 'TIE':
            self.type = 'tie'
            self.amount = int(s[1])
            self.actor = s[2]
        elif t == 'WIN':
            self.type = 'win'
            self.amount = int(s[1])
            self.actor = s[2]
