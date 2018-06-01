#blackjack.py

from random import randint
import sys

number = list(range(2,12))
suit = ['spade', 'heart', 'diamond', 'clover']

def drawcards():
    return [number[randint(0,len(number)-1)],suit[randint(0,len(suit)-1)]]

def restart():
    global pcard, pcount, dcards, dcount
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
    print('')

pcard = [drawcards(), drawcards()]
pcount = pcard[0][0] + pcard[1][0]
dcards = [drawcards(), drawcards()]
dcount = dcards[0][0] + dcards[1][0]
bid = 0

print('Welcome to BlackJack')
name = input("What's your name? ")
print('Hello ' + name)
print('Drawing card...' + '\n'*2)

while True:
    print(pcard)
    if dcount > 21: #dealer check 21
        print(dcards)
        print('Dealer went over 21 and you won!')
    answer = input('What would you like to do? (Hit, Stand, or Split) ')
    if pcount > 21: #player check 21
        print(pcard)
        print('You went over 21 and lost!')
        restart()
    if answer.lower() == 'hit': #player hit
        pcard.append(drawcards())
        pcount = pcount + pcard[-1][0]
        if pcount > 21:
            print(pcard)
            print('You went over 21 and lost!')
            restart()
    elif answer.lower() == 'stand': #player stand
        while dcount <= 13:
            dcards.append(drawcards())
            dcount = dcount + dcards[-1][0]
            print(dcount)
            if dcount > 21:
                print('You won!')
        print('\nDealer\'s hand: ' + str(dcards))
        if pcount > dcount:
            print('You won!')
        elif pcount == dcount:
            print('You tied!')
        else:
            print('You lost!')
        restart()
    elif answer.lower() == 'split': #player split
        pcard1 = [pcard[0]]
        pcard2 = [pcard[1]]
        pcard1.append(drawcards())
        pcard2.append(drawcards())
        pcount1 = pcard1[0][0] + pcard1[1][0]
        pcount2 = pcard2[0][0] + pcard2[1][0]
        while True:
            print('First: ', pcard1)
            print('Second: ', pcard2)
            if pcount1 > 21 or pcount2 > 21:
                print('You lost!')
                break
                restart()
            pc1 = input('What would you like to do for First? (Hit, Stand, or Split) ')
            if pc1.lower() == 'hit': #first split hit
                pcard1.append(drawcards())
                pcount1 += pcard1[-1][0]
                if pcount1 > 21:
                    print(pcard1)
                    print('You went over 21 and lost!')
                    restart()
            elif pc1.lower() == 'stand': #first split stand
                while dcount <= 13:
                    dcards.append(drawcards())
                    dcount = dcount + dcards[-1][0]
                    if dcount > 21:
                        print('Dealer went over 21 and you won!')
                        restart()
                    break
            pc2 = input('What would you like to do for Second? (Hit, Stand, or Split) ')        
            if pc2.lower() == 'hit': #second split hit
                pcard2.append(drawcards())
                pcount2 += pcard2[-1][0]
                if pcount2 > 21:
                    print(pcard2)
                    print('You went over 21 and lost!')
                    restart()
            elif pc2.lower() == 'stand': #second split stand
                while dcount <= 13:
                    dcards.append(drawcards())
                    dcount = dcount + dcards[-1][0]
                    if dcount > 21:
                        print('You won!')
                print('\nDealer\'s hand: ' + str(dcards))
                print('First hand: ' + str(pcard1))
                print('Second hand: ' + str(pcard2))
                print('\nFirst hand: ', end = '')
            if pcount1 > dcount:
                print('You won!')
            elif pcount1 == dcount:
                print('You tied!')
            else:
                print('You lost!')
            print('\nSecond hand: ', end = '')
            if pcount2 > dcount:
                print('You won!')
            elif pcount2 == dcount:
                print('You tied!')
            else:
                print('You lost!')
            restart()
            break
        
    else:
        print('Please enter Hit, Stand, or Split \n')
