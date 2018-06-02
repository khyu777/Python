#blackjack.py

from random import randint
import sys
    
class GameManager:

    number = list(range(2,12))
    suit = ['spade', 'heart', 'diamond', 'clover']

    def __init__(self):
        self.dcards = [self.drawcards(), self.drawcards()]
        self.dcount = self.dcards[0][0] + self.dcards[1][0]
        self.pcard = [self.drawcards(), self.drawcards()]
        self.pcount = self.pcard[0][0] + self.pcard[1][0]
        self.pcard1 = []
        self.pcard2 = []

    def drawcards(self):
        return [self.number[randint(0,len(self.number)-1)],self.suit[randint(0,len(self.suit)-1)]]

    def start(self):
        print('Welcome to BlackJack')
        name = input("What's your name? ")
        print('Hello ' + name)
        print('Drawing card...\n')

    def restart(self):
        again = input('\nWould you like to play again? (Y/N) ')
        if again.lower() == 'y':
            self.pcard = [self.drawcards(), self.drawcards()]
            self.pcount = self.pcard[0][0] + self.pcard[1][0]
            self.dcards = [self.drawcards(), self.drawcards()]
            self.dcount = self.dcards[0][0] + self.dcards[1][0]
        elif again.lower() == 'n':
            sys.exit()
        else:
            print('Please enter Y or N')
        print('')

    def dhit(self):
        while self.dcount <= 13:
            self.dcards.append(self.drawcards())
            self.dcount += self.dcards[-1][0]

    def dcheck(self):
        if self.dcount > 21:
            print('\nDealer\'s hand: ', dealer.dcards)
            print('Dealer went over 21 and you won!')
            self.restart()

    def phit(self):
        self.pcard.append(self.drawcards())
        self.pcount += self.pcard[-1][0]

    def stand(self):
        if self.pcount > self.dcount:
            print('You won!')
        elif self.pcount == self.dcount:
            print('You tied!')
        else:
            print('You lost!')
    
    def split(self):
        self.pcard1 = [self.pcard[0]]
        self.pcard2 = [self.pcard[1]]
        self.pcard1.append(self.drawcards())
        self.pcard2.append(self.drawcards())
        self.pcount1 = self.pcard1[0][0] + self.pcard1[1][0]
        self.pcount2 = self.pcard2[0][0] + self.pcard2[1][0]

    def pcheck(self):
        if self.pcount > 21:
            print('\nYour hand: ', self.pcard)
            print('You went over 21 and lost!')
            self.restart()

game = GameManager()
game.start()

while True:
    print(game.pcard)
    game.pcheck()
    game.dcheck()
    answer = input('What would you like to do? (Hit, Stand, or Split) ').lower()
    if answer == 'hit':
        game.phit()
        game.pcheck()
    elif answer == 'stand':
        game.dhit()
        game.dcheck()
        print('\nYour hand: ', game.pcard)
        print('Dealer\'s hand: ', game.dcards)
        game.stand()
        game.restart()
    elif answer == 'split':
        game.split()
        while True:
            print('First: ', game.pcard1)
            print('Second: ', game.pcard2)
#fix below
            if pcount1 > 21 or pcount2 > 21:
                print('You lost!')
                break
                game.restart()
            pc1 = input('What would you like to do for First? (Hit, Stand, or Split) ')
            if pc1.lower() == 'hit': #first split hit
                pcard1.append(game.drawcards())
                pcount1 += pcard1[-1][0]
                if pcount1 > 21:
                    print(pcard1)
                    print('You went over 21 and lost!')
                    game.restart()
            elif pc1.lower() == 'stand': #first split stand
                while dcount <= 13:
                    dcards.append(game.drawcards())
                    dcount = dcount + dcards[-1][0]
                    if dcount > 21:
                        print('Dealer went over 21 and you won!')
                        game.restart()
                    break
            pc2 = input('What would you like to do for Second? (Hit, Stand, or Split) ')        
            if pc2.lower() == 'hit': #second split hit
                pcard2.append(game.drawcards())
                pcount2 += pcard2[-1][0]
                if pcount2 > 21:
                    print(pcard2)
                    print('You went over 21 and lost!')
                    game.restart()
            elif pc2.lower() == 'stand': #second split stand
                while dcount <= 13:
                    dcards.append(game.drawcards())
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
            game.restart()
            break
        
    else:
        print('Please enter Hit, Stand, or Split \n')
