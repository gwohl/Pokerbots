#from pokereval import PokerEval
#POKER = PokerEval()
def makePreFlopTable3():
    a = {}
    a['AAo'] = .73444
    a['AKs'] = .50733
    a['AQs'] = .49433
    a['AJs'] = .48174
    a['ATs'] = .47049
    a['A9s'] = .44552
    a['A8s'] = .43494
    a['A7s'] = .42390
    a['A6s'] = .41168
    a['A5s'] = .41434
    a['A4s'] = .40496
    a['A3s'] = .39685
    a['A2s'] = .38781
    a['AKo'] = .48183
    a['KKo'] = .68899
    a['KQs'] = .47039
    a['KJs'] = .45881
    a['KTs'] = .44793
    a['K9s'] = .42313
    a['K8s'] = .40143
    a['K7s'] = .39264
    a['K6s'] = .38279
    a['K5s'] = .37410
    a['K4s'] = .36537
    a['K3s'] = .35705
    a['K2s'] = .34911
    a['AQo'] = .46803
    a['KQo'] = .44403
    a['QQo'] = .64932
    a['QJs'] = .44214
    a['QTs'] = .43108
    a['Q9s'] = .40642
    a['Q8s'] = .38502
    a['Q7s'] = .36485
    a['Q6s'] = .35710
    a['Q5s'] = .34846
    a['Q4s'] = .34015
    a['Q3s'] = .33187
    a['Q2s'] = .32425
    a['AJo'] = .45495
    a['KJo'] = .43136
    a['QJo'] = .41366
    a['JJo'] = .61161
    a['JTs'] = .41940
    a['J9s'] = .39465
    a['J8s'] = .37397
    a['J7s'] = .35360
    a['J6s'] = .33381
    a['J5s'] = .32375
    a['J4s'] = .31904
    a['J3s'] = .31135
    a['J2s'] = .30356
    a['ATo'] = .44285
    a['KTo'] = .41900
    a['QTo'] = .40193
    a['JTo'] = .39015
    a['TTo'] = .57583
    a['T9s'] = .38779
    a['T8s'] = .36655
    a['T7s'] = .34655
    a['T6s'] = .32689
    a['T5s'] = .30768
    a['T4s'] = .30186
    a['T3s'] = .29423
    a['T2s'] = .28664
    a['A9o'] = .41572
    a['K9o'] = .39240
    a['Q9o'] = .37549
    a['J9o'] = .36368
    a['T9o'] = .35669
    a['99o'] = .53611
    a['98s'] = .35949
    a['97s'] = .34073
    a['96s'] = .32168
    a['95s'] = .30260
    a['94s'] = .28355
    a['93s'] = .27836
    a['92s'] = .27072
    a['A8o'] = .40483
    a['K8o'] = .36920
    a['Q8o'] = .35287
    a['J8o'] = .34123
    a['T8o'] = .33426
    a['98o'] = .32696
    a['88o'] = .49922
    a['87s'] = .33792
    a['86s'] = .31936
    a['85s'] = .30067
    a['84s'] = .28193
    a['83s'] = .26346
    a['82s'] = .25829
    a['A7o'] = .39243
    a['K7o'] = .35964
    a['Q7o'] = .33056
    a['J7o'] = .31924
    a['T7o'] = .31261
    a['97o'] = .30672
    a['87o'] = .30408
    a['77o'] = .46434
    a['76s'] = .31896
    a['75s'] = .30127
    a['74s'] = .28248
    a['73s'] = .26409
    a['72s'] = .24576
    a['A6o'] = .37939
    a['K6o'] = .34886
    a['Q6o'] = .32220
    a['J6o'] = .29770
    a['T6o'] = .29120
    a['96o'] = .28609
    a['86o'] = .28386
    a['76o'] = .28406
    a['66o'] = .43174
    a['65s'] = .30271
    a['64s'] = .28504
    a['63s'] = .26682
    a['62s'] = .24808
    a['A5o'] = .38178
    a['K5o'] = .33951
    a['Q5o'] = .31301
    a['J5o'] = .29126
    a['T5o'] = .27078
    a['95o'] = .26550
    a['85o'] = .26422
    a['75o'] = .26485
    a['65o'] = .26661
    a['55o'] = .40067
    a['54s'] = .29025
    a['53s'] = .27259
    a['52s'] = .25440
    a['A4o'] = .37173
    a['K4o'] = .32976
    a['Q4o'] = .30359
    a['J4o'] = .28198
    a['T4o'] = .26417
    a['94o'] = .24514
    a['84o'] = .24357
    a['74o'] = .24459
    a['64o'] = .24762
    a['54o'] = .25338
    a['44o'] = .36752
    a['43s'] = .26438
    a['42s'] = .24691
    a['A3o'] = .36296
    a['K3o'] = .32072
    a['Q3o'] = .29485
    a['J3o'] = .27347
    a['T3o'] = .25574
    a['93o'] = .23918
    a['83o'] = .22375
    a['73o'] = .22464
    a['63o'] = .22785
    a['53o'] = .23439
    a['43o'] = .22570
    a['33o'] = .33640
    a['32s'] = .23862
    a['A2o'] = .35242
    a['K2o'] = .31200
    a['Q2o'] = .28625
    a['J2o'] = .26477
    a['T2o'] = .24745
    a['92o'] = .23096
    a['82o'] = .21797
    a['72o'] = .20477
    a['62o'] = .20770
    a['52o'] = .21491
    a['42o'] = .20641
    a['32o'] = .19759
    a['22o'] = .30656

    return a


def makePreFlopTable2():
    a = {}
    a['AAo'] = .85203
    a['AKs'] = .67045
    a['AQs'] = .66209
    a['AJs'] = .65393
    a['ATs'] = .64602
    a['A9s'] = .62781
    a['A8s'] = .61944
    a['A7s'] = .60984
    a['A6s'] = .59906
    a['A5s'] = .59923
    a['A4s'] = .59034
    a['A3s'] = .58220
    a['A2s'] = .57379
    a['AKo'] = .65320
    a['KKo'] = .82396
    a['KQs'] = .63400
    a['KJs'] = .62567
    a['KTs'] = .61789
    a['K9s'] = .59988
    a['K8s'] = .58312
    a['K7s'] = .57538
    a['K6s'] = .56641
    a['K5s'] = .55793
    a['K4s'] = .54885
    a['K3s'] = .54055
    a['K2s'] = .53212
    a['AQo'] = .64432
    a['KQo'] = .61456
    a['QQo'] = .79925
    a['QJs'] = .60259
    a['QTs'] = .59468
    a['Q9s'] = .57664
    a['Q8s'] = .56018
    a['Q7s'] = .54302
    a['Q6s'] = .53613
    a['Q5s'] = .52762
    a['Q4s'] = .51855
    a['Q3s'] = .51019
    a['Q2s'] = .50169
    a['AJo'] = .63563
    a['KJo'] = .60569
    a['QJo'] = .58135
    a['JJo'] = .77469
    a['JTs'] = .57528
    a['J9s'] = .55662
    a['J8s'] = .54016
    a['J7s'] = .52325
    a['J6s'] = .50606
    a['J5s'] = .49987
    a['J4s'] = .49070
    a['J3s'] = .48232
    a['J2s'] = .47378
    a['ATo'] = .62722
    a['KTo'] = .59739
    a['QTo'] = .57291
    a['JTo'] = .55248
    a['TTo'] = .75012
    a['T9s'] = .54028
    a['T8s'] = .52334
    a['T7s'] = .50639
    a['T6s'] = .48941
    a['T5s'] = .47216
    a['T4s'] = .46530
    a['T3s'] = .45693
    a['T2s'] = .44839
    a['A9o'] = .60773
    a['K9o'] = .57812
    a['Q9o'] = .55360
    a['J9o'] = .53251
    a['T9o'] = .51532
    a['99o'] = .72057
    a['98s'] = .50801
    a['97s'] = .49118
    a['96s'] = .47428
    a['95s'] = .45722
    a['94s'] = .43862
    a['93s'] = .43264
    a['92s'] = .42415
    a['A8o'] = .59873
    a['K8o'] = .56020
    a['Q8o'] = .53600
    a['J8o'] = .51490
    a['T8o'] = .49721
    a['98o'] = .48097
    a['88o'] = .69163
    a['87s'] = .47936
    a['86s'] = .46243
    a['85s'] = .44545
    a['84s'] = .42702
    a['83s'] = .40874
    a['82s'] = .40272
    a['A7o'] = .58841
    a['K7o'] = .55187
    a['Q7o'] = .51766
    a['J7o'] = .49682
    a['T7o'] = .47908
    a['97o'] = .46298
    a['87o'] = .45051
    a['77o'] = .66236
    a['76s'] = .45372
    a['75s'] = .43676
    a['74s'] = .41849
    a['73s'] = .40036
    a['72s'] = .38156
    a['A6o'] = .57682
    a['K6o'] = .54223
    a['Q6o'] = .51024
    a['J6o'] = .47844
    a['T6o'] = .46092
    a['96o'] = .44491
    a['86o'] = .43241
    a['76o'] = .42323
    a['66o'] = .63285
    a['65s'] = .43133
    a['64s'] = .41333
    a['63s'] = .39534
    a['62s'] = .37669
    a['A5o'] = .57697
    a['K5o'] = .53314
    a['Q5o'] = .50120
    a['J5o'] = .47181
    a['T5o'] = .44251
    a['95o'] = .42669
    a['85o'] = .41428
    a['75o'] = .40512
    a['65o'] = .39944
    a['55o'] = .60325
    a['54s'] = .41453
    a['53s'] = .39693
    a['52s'] = .37849
    a['A4o'] = .56730
    a['K4o'] = .52327
    a['Q4o'] = .49128
    a['J4o'] = .46186
    a['T4o'] = .43504
    a['94o'] = .40671
    a['84o'] = .39447
    a['74o'] = .38550
    a['64o'] = .38010
    a['54o'] = .38155
    a['44o'] = .57023
    a['43s'] = .38642
    a['42s'] = .36829
    a['A3o'] = .55845
    a['K3o'] = .51426
    a['Q3o'] = .48219
    a['J3o'] = .45276
    a['T3o'] = .42595
    a['93o'] = .40020
    a['83o'] = .37484
    a['73o'] = .36602
    a['63o'] = .36078
    a['53o'] = .36265
    a['43o'] = .35146
    a['33o'] = .53693
    a['32s'] = .35984
    a['A2o'] = .54929
    a['K2o'] = .50509
    a['Q2o'] = .47295
    a['J2o'] = .44348
    a['T2o'] = .41668
    a['92o'] = .39098
    a['82o'] = .36828
    a['72o'] = .34584
    a['62o'] = .34075
    a['52o'] = .34285
    a['42o'] = .33200
    a['32o'] = .32303
    a['22o'] = .50334

    return a


def getPreflopString(hand):
	suited = 'o'
	returnString = ''
	if hand[0][1:] == hand[1][1:]:
		suited = 's'
	firstCard = hand[0][0:1]
	secondCard = hand[1][0:1]
	returnString = firstCard + secondCard
	firstNum = 0
	secondNum = 0
	if firstCard == 'A':
		firstNum = 14
	elif firstCard == 'K':
		firstNum = 13
	elif firstCard == 'Q':
		firstNum = 12
	elif firstCard == 'J':
		firstNum = 11
	elif firstCard == 'T':
		firstNum = 10
	else:
	    firstNum = int(firstCard)
	if secondCard == 'A':
		secondNum = 14
	elif secondCard == 'K':
		secondNum = 13
	elif secondCard == 'Q':
		secondNum = 12
	elif secondCard == 'J':
		secondNum = 11
	elif secondCard == 'T':
		secondNum = 10
	else:
	    secondNum = int(secondCard)
	if secondNum > firstNum:
		returnString = secondCard + firstCard
	returnString += suited
	return returnString
	
def computeHandScore(hand,board,POKER):
    score = 0
    knownCards = hand + board
    currentBest = POKER.best("hi",knownCards)
    altScoreSet = []
    totalPossibilities = 0
    if len(board) == 3:
        totalPossibilities = 47*46
        for i in range(0,52):
            for j in range(0,i):
                firstCard = POKER.card2string(i)
                secondCard = POKER.card2string(j)
                if firstCard not in knownCards and secondCard not in knownCards:
                    scoreAdd = POKER.best("hi",knownCards+[firstCard] + [secondCard])[0] #Change when we have equity table
                    if scoreAdd > currentBest[0]:
                        altScoreSet.append(scoreAdd)
    else:
        totalPossibilities = 46
        for i in POKER.card2string(range(0,52)):
            if i not in knownCards:
                scoreAdd = POKER.best("hi",knownCards+[i])[0] #Change when we have equity table
                if scoreAdd > currentBest[0]:
                    altScoreSet.append(scoreAdd)
    numAlts = len(altScoreSet)
    for altScore in altScoreSet:
        score += altScore*1.0/totalPossibilities
    score += currentBest[0]*float(totalPossibilities-numAlts)/float(totalPossibilities)#Change when we have equity table
    return score


def probOfWin(POKER, hand, boardCards, leftPlayerIn, rightPlayerIn, diff):
    if leftPlayerIn and rightPlayerIn:
        if len(boardCards) == 3:
            prob = float(POKER.poker_eval(game = 'holdem', pockets = [hand,[255,255],[255,255]], dead = [], board = boardCards + [255,255], iterations = 100000)['eval'][0]['winhi'])/100000
        elif len(boardCards) == 4:
            prob = float(POKER.poker_eval(game = 'holdem', pockets = [hand,[255,255],[255,255]], dead = [], board = boardCards + [255], iterations = 100000)['eval'][0]['winhi'])/100000
        else:
            prob = float(POKER.poker_eval(game = 'holdem', pockets = [hand,[255,255],[255,255]], dead = [], board = boardCards, iterations = 100000)['eval'][0]['winhi'])/100000
    else:
        if len(boardCards) == 3:
            prob = float(POKER.poker_eval(game = 'holdem', pockets = [hand,[255,255]], dead = [], board = boardCards + [255,255], iterations = 100000)['eval'][0]['winhi'])/100000
        elif len(boardCards) == 4:
            prob = float(POKER.poker_eval(game = 'holdem', pockets = [hand,[255,255]], dead = [], board = boardCards + [255], iterations = 100000)['eval'][0]['winhi'])/100000
        else:
            prob = float(POKER.poker_eval(game = 'holdem', pockets = [hand,[255,255]], dead = [], board = boardCards, iterations = 100000)['eval'][0]['winhi'])/100000
    probBetterHand = numBetterHands(POKER,hand,boardCards)[1]
    if leftPlayerIn and rightPlayerIn:
        newProb = prob * (1 - probBetterHand)**2
    else:
        newProb = prob * (1 - probBetterHand)
    if diff > 0:
        return (prob + newProb)/2
    else:
        return .9 * (prob + newProb)/2



def numBetterHands(POKER, hand, boardCards):
    bestHandScore = POKER.best('hi', hand + boardCards)[0]
    counter = 0
    for i in range(52):
        for j in range(i):
            if POKER.card2string(i) not in hand + boardCards and POKER.card2string(j) not in hand + boardCards:
                opHand = [POKER.card2string(i),POKER.card2string(j)]
                opScore = POKER.best('hi', boardCards + opHand)[0]
                if opScore > bestHandScore:
                    counter += 1
    availCards = 52 - 2 - len(boardCards)
    hands = availCards * (availCards-1) /2
    return counter, float(counter)/hands


            
        
            
            
            
