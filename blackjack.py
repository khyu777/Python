#blackjack.py

from random import randint
import sys
    
class GameManager:

    number = list(range(2,12))
    letter = [['J',10], ['Q',10], ['K',10], ['A',11]]
    suit = ['spade', 'heart', 'diamond', 'clover']

    def __init__(self):
        self.dcards = [self.drawcards(), self.drawcards()]
        self.pcard = [self.drawcards(), self.drawcards()]
        self.pcard1 = []
        self.pcard2 = []
        self.setdcount()
        self.setpcount()
        self.bank = 1000

    def drawcards(self):
        randnum = self.number[randint(0,len(self.number)-1)]
        randsuit = self.suit[randint(0,len(self.suit)-1)]
        if randnum == 10:
            return [self.letter[randint(0,2)],randsuit]
        elif randnum == 11:
            return [self.letter[3], randsuit]
        else:
            return [randnum, randsuit]

    def start(self):
        print('Welcome to BlackJack')
        name = input("What's your name? ")
        print('Hello ' + name)
        print('Drawing card...\n')

    def restart(self):
        while True:
            again = input('\nWould you like to play again? (Y/N) ')
            if again.lower() == 'y':
                self.pcard = [self.drawcards(), self.drawcards()]
                self.setpcount()
                self.dcards = [self.drawcards(), self.drawcards()]
                self.setdcount()
                break
            elif again.lower() == 'n':
                sys.exit()
            else:
                print('Please enter Y or N')
            print('')
        self.pbet()

    #Dealer

    def dcheck(self):
        if self.dcount > 21:
            print('\nDealer\'s hand: ', self.dcards)
            print('Dealer went over 21 and you won!')
            self.bank += self.bet
            self.restar()
            
    def dhit(self):
        while self.dcount <= 13:
            self.dcards.append(self.drawcards())
            if isinstance(self.dcards[-1][0], list) == True:
                self.dcount += self.dcards[-1][0][1]
            else:
                self.dcount += self.dcards[-1][0]

    def setdcount(self):
        if isinstance(self.dcards[0][0], list) == True and isinstance(self.dcards[1][0], list) == True:
            self.dcount = self.dcards[0][0][1] + self.dcards[1][0][1]
        elif isinstance(self.dcards[0][0], list) == True and isinstance(self.dcards[1][0], list) == False:
            self.dcount = self.dcards[0][0][1] + self.dcards[1][0]
        elif isinstance(self.dcards[0][0], list) == False and isinstance(self.dcards[1][0], list) == True:
            self.dcount = self.dcards[0][0] + self.dcards[1][0][1]
        else:
            self.dcount = self.dcards[0][0] + self.dcards[1][0]

    #Player
     
    def pcheck(self):
        if self.pcount > 21:
            print('\nYour hand: ', self.pcard)
            print('You went over 21 and lost!')
            self.bank -= self.bet
            self.bankrupt()
            self.restart()
       
    def pbet(self):
        print('You currently have', '$' + str(self.bank), 'in your bank.')
        while True:
            self.bet = input('\nHow much would you like to bet?: ')
            if self.bet.isdigit() == True:
                self.bet = int(self.bet)
                if self.bet == 0:
                    print('You can\'t bet nothing')
                elif self.bet > self.bank:
                    print('Insufficient fund in bank')
                elif self.bet <= self.bank:
                    break
            else:
                print('Please enter a valid number')
                
    def phit(self):
        self.pcard.append(self.drawcards())
        if isinstance(self.pcard[-1][0], list) == True:
            self.pcount += self.pcard[-1][0][1]
        else:
            self.pcount += self.pcard[-1][0]

    def stand(self):
        if self.pcount > self.dcount:
            print('You won!')
            self.bank += self.bet
        elif self.pcount == self.dcount:
            print('You tied!')
        else:
            print('You lost!')
            self.bank -= self.bet
            self.bankrupt()
    
    def split(self):
        self.pcard1 = [self.pcard[0]]
        self.pcard2 = [self.pcard[1]]
        self.pcard1.append(self.drawcards())
        self.pcard2.append(self.drawcards())
        self.pcount1 = self.pcard1[0][0] + self.pcard1[1][0]
        self.pcount2 = self.pcard2[0][0] + self.pcard2[1][0]

    def setpcount(self):
        if isinstance(self.pcard[0][0], list) == True and isinstance(self.pcard[1][0], list) == True:
            self.pcount = self.pcard[0][0][1] + self.pcard[1][0][1]
        elif isinstance(self.pcard[0][0], list) == True and isinstance(self.pcard[1][0], list) == False:
            self.pcount = self.pcard[0][0][1] + self.pcard[1][0]
        elif isinstance(self.pcard[0][0], list) == False and isinstance(self.pcard[1][0], list) == True:
            self.pcount = self.pcard[0][0] + self.pcard[1][0][1]
        else:
            self.pcount = self.pcard[0][0] + self.pcard[1][0]
            
    def checkA(self):
        for i in range(2):
            if isinstance(self.pcard[i][0], list) == True:
                while True:
                    if self.pcard[i][0][0] == 'A':
                        ainput = input('1 or 11? ')
                        if ainput == '1':
                            self.pcard[i][0][1] = 1
                            print('\n')
                            print(self.pcard)
                            break
                        elif ainput == '11':
                            self.pcard[i][0][1] = 11
                            print('\n')
                            print(self.pcard)
                            break
                        else:
                            print('Please enter 1 or 11')

    def bankrupt(self):
        if self.bank == 0:
            print('You went bankrupt!')
            self.bank = 1000
                
game = GameManager()
game.start()
game.pbet()
count = 0

while True:
    print(game.pcard)
    if count == 0:
        game.checkA()
        game.setdcount()
        game.setpcount()
        count += 1
    game.pcheck()
    game.dcheck()
    answer = input('\nWhat would you like to do? (Hit, Stand, or Split) ').lower()
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
        count = 0
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
