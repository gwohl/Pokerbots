import random


### Run Monte Carlo simulations for starting Pre-flop hands

"""

       2h/00  2d/13  2c/26  2s/39
       3h/01  3d/14  3c/27  3s/40
       4h/02  4d/15  4c/28  4s/41
       5h/03  5d/16  5c/29  5s/42
       6h/04  6d/17  6c/30  6s/43
       7h/05  7d/18  7c/31  7s/44
       8h/06  8d/19  8c/32  8s/45
       9h/07  9d/20  9c/33  9s/46
       Th/08  Td/21  Tc/34  Ts/47
       Jh/09  Jd/22  Jc/35  Js/48
       Qh/10  Qd/23  Qc/36  Qs/49
       Kh/11  Kd/24  Kc/37  Ks/50
       Ah/12  Ad/25  Ac/38  As/51
"""

## Hand shortcuts


## Will return a hand of three random cards with d1,d2,d3 as deadcards
def draw_hands(d1=52, d2=52, d3=52):
    topop = sorted([d1,d2,d3])
    deck = range(55)
    deck.pop(topop[2])
    deck.pop(topop[1])
    deck.pop(topop[0])       
    
    hand = []
    card1 = deck.pop(random.randint(0,51))
    card2 = deck.pop(random.randint(0,50))
    card3 = deck.pop(random.randint(0,49))

    return [card1, card2, card3]
    

##Takes in a hand, defined to be a list of three unique numbers between 0 and 52)
def hand_eval(hand, times):
    deck = range(52)
    









    
    
    
