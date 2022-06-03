import rock 
import random

print('The game is about to begin !!!')
name = input ('Please enter your name : ')

print ('Pick a hand : (0: Rock , 1: Paper , 2: Scissors )' )
playerHand = int(input('Please enter a number (0-2): '))

if rock.value(playerHand):
    computerHand = random.randint(0,2)

    rock.printHand(playerHand, name)
    rock.printHand(computerHand,'Computer')

    result = rock.check(playerHand,computerHand)
    print('Result:' + result )

else:
    print('Please  enter a valid number')