


##Semi-smart All-in Bot

def convert(card):
    if card[0] == "J":
        return "11"+card[1]
    elif card[0] == "Q":
        return "12"+card[1]
    elif card[0] == "K":
        return "13"+card[1]
    elif card[0] == "A":
        return "14" + card[1]
    else:
        return card

def cardval(s):
    return s[0]

##List of hole cards
def semiAIB(hole):
    converted = []
    for z in range(3):
        converted.append(convert(hole[z]))
    newcards = sorted(converted, key=cardval)
    if int(newcards[2][:-1]) - int(newcards[1][:-1]) >=5 and int(newcards[1][:-1]) - int(newcards[0][:-1])>=5:
        if newcards[2][1] != newcards[1][1] != newcards[0][1]:
            return "Fold"
        else:
            return "Call"
    else:
        return "Call"
