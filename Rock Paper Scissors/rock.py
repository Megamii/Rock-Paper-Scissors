def value(hand):
    if hand < 0 or hand > 2:
        return False 
    return True 

def printHand(hand, name = 'Guest'):
    hands = ['Rock','Paper','Scissors']
    print (name + ' picked: ' + hands[hand])

def check(player, computer):
    if player == computer:
       return "It's a draw!"

    elif player == 0 and computer ==1:
        return 'You Lose'

    elif player == 1 and computer ==2:
        return 'You Lose'

    elif player == 2 and computer ==0:
        return 'You Lose'
    else:
        return ('Yayy!!! You Won')


