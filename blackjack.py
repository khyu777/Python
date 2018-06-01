#blackjack.py

from random import randint
import sys

number = list(range(2,12))
suit = ['spade', 'heart', 'diamond', 'clover']

def drawcards():
    return [number[randint(0,len(number)-1)],suit[randint(0,len(suit)-1)]]

pcard = [drawcards(), drawcards()]
pcount = pcard[0][0] + pcard[1][0]
dcards = [drawcards(), drawcards()]
dcount = dcards[0][0] + dcards[1][0]

print('Welcome to BlackJack')
name = input("What's your name? ")
print('Hello ' + name)
print('Drawing card...' + '\n'*2)

while True:
    print(pcard)
    if dcount > 21:
        print('Dealer lost!')
    answer = input('What would you like to do? (Hit, Stand, or Split) ')
    if answer.lower() == 'hit':
        pcard.append(drawcards())
        pcount = pcount + pcard[-1][0]
        if pcount > 21:
            print(pcard)
            print('You went over 21 and lost!')
            while True:
                again = input('\nWould you like to play again? (Y/N) ')
                if again.lower() == 'y':
                    pcard = [drawcards(), drawcards()]
                    pcount = pcard[0][0] + pcard[1][0]
                    dcards = [drawcards(), drawcards()]
                    dcount = dcards[0][0] + dcards[1][0]
                    break
                elif again.lower() == 'n':
                    sys.exit()
                else:
                    print('Please enter Y or N')
    elif answer.lower() == 'stand':
        while dcount <= 13:
            dcards.append(drawcards())
            dcount = dcount + dcards[-1][0]
            if dcount > 21:
                print('You won!')
        print('\nDealer\'s hand: ' + str(dcards))
        if pcount > dcount:
            print('You won!')
        elif pcount == dcount:
            print('You tied!')
        else:
            print('You lost!')
        while True:
            again = input('\nWould you like to play again? (Y/N) ')
            if again.lower() == 'y':
                pcard = [drawcards(), drawcards()]
                pcount = pcard[0][0] + pcard[1][0]
                dcards = [drawcards(), drawcards()]
                dcount = dcards[0][0] + dcards[1][0]
                break
            elif again.lower() == 'n':
                sys.exit()
            else:
                print('Please enter Y or N')
    elif answer.lower() == 'split':
        pcard1 = [pcard[0]]
        pcard2 = [pcard[1]]
        pcount1 = pcard1[0][0]
        pcount2 = pcard2[0][0]
        restart = 0
        while restart == 0:
            print('First: ', pcard1)
            print('Second: ', pcard2)
            pc1 = input('What would you like to do for First? (Hit, Stand, or Split) ')
            if pc1.lower() == 'hit':
                pcard1.append(drawcards())
                pcount1 += pcard[-1][0]
                if pcount1 > 21:
                    print(pcard1)
                    print('You went over 21 and lost!')
                    while True:
                        again = input('\nWould you like to play again? (Y/N) ')
                        if again.lower() == 'y':
                            pcard = [drawcards(), drawcards()]
                            pcount = pcard[0][0] + pcard[1][0]
                            dcards = [drawcards(), drawcards()]
                            dcount = dcards[0][0] + dcards[1][0]
                            break
                        elif again.lower() == 'n':
                            sys.exit()
                        else:
                                print('Please enter Y or N')
            elif pc1.lower() == 'stand':
                while dcount <= 13:
                    dcards.append(drawcards())
                    dcount = dcount + dcards[-1][0]
                    if dcount > 21:
                        print('You won!')
                print('\nDealer\'s hand: ' + str(dcards))
                if pcount1 > dcount:
                    print('You won!')
                elif pcount1 == dcount:
                    print('You tied!')
                else:
                    print('You lost!')
                while True:
                    again = input('\nWould you like to play again? (Y/N) ')
                    if again.lower() == 'y':
                        pcard = [drawcards(), drawcards()]
                        pcount = pcard[0][0] + pcard[1][0]
                        dcards = [drawcards(), drawcards()]
                        dcount = dcards[0][0] + dcards[1][0]
                        restart += 1
                        print(restart)
                        break
                    elif again.lower() == 'n':
                        sys.exit()
                    else:
                        print('Please enter Y or N')
            pc2 = input('What would you like to do for Second? (Hit, Stand, or Split) ')        
            if pc2.lower() == 'hit':
                pcard2.append(drawcards())
                pcount2 += pcard[-1][0]
                if pcount2 > 21:
                    print(pcard2)
                    print('You went over 21 and lost!')
                    while True:
                        again = input('\nWould you like to play again? (Y/N) ')
                        if again.lower() == 'y':
                            pcard = [drawcards(), drawcards()]
                            pcount = pcard[0][0] + pcard[1][0]
                            dcards = [drawcards(), drawcards()]
                            dcount = dcards[0][0] + dcards[1][0]
                            break
                        elif again.lower() == 'n':
                            sys.exit()
                        else:
                                print('Please enter Y or N')
            elif pc2.lower() == 'stand':
                while dcount <= 13:
                    dcards.append(drawcards())
                    dcount = dcount + dcards[-1][0]
                    if dcount > 21:
                        print('You won!')
                print('\nDealer\'s hand: ' + str(dcards))
                if pcount2 > dcount:
                    print('You won!')
                elif pcount2 == dcount:
                    print('You tied!')
                else:
                    print('You lost!')
                while True:
                    again = input('\nWould you like to play again? (Y/N) ')
                    if again.lower() == 'y':
                        pcard = [drawcards(), drawcards()]
                        pcount = pcard[0][0] + pcard[1][0]
                        dcards = [drawcards(), drawcards()]
                        dcount = dcards[0][0] + dcards[1][0]
                        break
                    elif again.lower() == 'n':
                        sys.exit()
                    else:
                        print('Please enter Y or N')
            
    else:
        print('Please enter Hit, Stand, or Split \n')
