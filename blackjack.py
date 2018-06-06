#blackjack.py

from random import randint
import sys
    
class GameManager:

    number = list(range(2,12))
    letter = [['J',10], ['Q',10], ['K',10], ['A',11]]
    suit = ['spade', 'heart', 'diamond', 'clover']

    def __init__(self):
        self.pcard1 = []
        self.pcard2 = []
        self.counter = 0

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
                player.cards = [self.drawcards(), self.drawcards()]
                player.setcount()
                dealer.cards = [self.drawcards(), self.drawcards()]
                dealer.setcount()
                break
            elif again.lower() == 'n':
                sys.exit()
            else:
                print('Please enter Y or N')
            print('')
        player.bet()
        self.counter = 0

class Dealer(GameManager):

    def __init__(self):
        self.cards = [GameManager.drawcards(self), GameManager.drawcards(self)]
        self.setcount()
            
    def check(self):
        if self.count > 21:
            print('\nDealer\'s hand: ', self.cards)
            print('Dealer went over 21 and you won!')
            player.bank += player.bid
            self.restart()
            
    def hit(self):
        while self.count <= 13:
            self.cards.append(self.drawcards())
            if isinstance(self.cards[-1][0], list) == True:
                self.count += self.cards[-1][0][1]
            else:
                self.count += self.cards[-1][0]

    def setcount(self):
        if isinstance(self.cards[0][0], list) == True and isinstance(self.cards[1][0], list) == True:
            self.count = self.cards[0][0][1] + self.cards[1][0][1]
        elif isinstance(self.cards[0][0], list) == True and isinstance(self.cards[1][0], list) == False:
            self.count = self.cards[0][0][1] + self.cards[1][0]
        elif isinstance(self.cards[0][0], list) == False and isinstance(self.cards[1][0], list) == True:
            self.count = self.cards[0][0] + self.cards[1][0][1]
        else:
            self.count = self.cards[0][0] + self.cards[1][0]

class Player(GameManager):
     
    def __init__(self):
        self.cards = [GameManager.drawcards(self), GameManager.drawcards(self)]
        self.bank = 1000
        self.setcount() 

    def check(self):
        if self.count > 21:
            print('\nYour hand: ', self.cards)
            print('You went over 21 and lost!')
            self.bank -= self.bid
            self.bankrupt()
            self.restart()
            game.counter = 0
       
    def bet(self):
        print('You currently have', '$' + str(self.bank), 'in your bank.')
        while True:
            self.bid = input('\nHow much would you like to bet?: ')
            if self.bid.isdigit() == True:
                self.bid = int(self.bid)
                if self.bid == 0:
                    print('You can\'t bet nothing')
                elif self.bid > self.bank:
                    print('Insufficient fund in bank')
                elif self.bid <= self.bank:
                    break
            else:
                print('Please enter a valid number')
                
    def hit(self):
        self.cards.append(self.drawcards())
        if isinstance(self.cards[-1][0], list) == True:
            self.count += self.cards[-1][0][1]
        else:
            self.count += self.cards[-1][0]

    def stand(self):
        dealer.hit()
        dealer.check()
        if self.count > dealer.count:
            print('You won!')
            self.bank += self.bid
        elif self.count == dealer.count:
            print('You tied!')
        else:
            print('You lost!')
            self.bank -= self.bid
            self.bankrupt()
        self.restart()

    def split(self):
        self.pcard1 = [self.cards[0]]
        self.pcard2 = [self.cards[1]]
        self.pcard1.append(self.drawcards())
        self.pcard2.append(self.drawcards())
        self.pcount1 = self.pcard1[0][0] + self.pcard1[1][0]
        self.pcount2 = self.pcard2[0][0] + self.pcard2[1][0]

    def setcount(self):
        if isinstance(self.cards[0][0], list) == True and isinstance(self.cards[1][0], list) == True:
            self.count = self.cards[0][0][1] + self.cards[1][0][1]
        elif isinstance(self.cards[0][0], list) == True and isinstance(self.cards[1][0], list) == False:
            self.count = self.cards[0][0][1] + self.cards[1][0]
        elif isinstance(self.cards[0][0], list) == False and isinstance(self.cards[1][0], list) == True:
            self.count = self.cards[0][0] + self.cards[1][0][1]
        else:
            self.count = self.cards[0][0] + self.cards[1][0]
            
    def checkA(self):
        for i in range(2):
            if isinstance(self.cards[i][0], list) == True:
                while True:
                    if self.cards[i][0][0] == 'A':
                        ainput = input('1 or 11? ')
                        if ainput == '1':
                            self.cards[i][0][1] = 1
                            print('\n')
                            print(self.cards)
                            break
                        elif ainput == '11':
                            self.cards[i][0][1] = 11
                            print('\n')
                            print(self.cards)
                            break
                        else:
                            print('Please enter 1 or 11')
                    else:
                        break

    def bankrupt(self):
        if self.bank == 0:
            print('You went bankrupt!')
            self.bank = 1000
if __name__ == "__main__":       
    game = GameManager()
    dealer = Dealer()
    player = Player()
    game.start()
    player.bet()

while True:
    print(player.cards)
    if game.counter == 0:
        player.checkA()
        dealer.setcount()
        player.setcount()
        game.counter += 1
    player.check()
    dealer.check()
    answer = input('\nWhat would you like to do? (Hit, Stand, or Split) ').lower()
    if answer == 'hit':
        # print('hit')
        player.hit()
        player.check()
        # print('hit end')
    elif answer == 'stand':
        # print('stand')
        print('\nYour hand: ', player.cards)
        print('Dealer\'s hand: ', dealer.cards)
        player.stand()
        game.counter = 0
        # print('stand end')
    elif answer == 'split':
        player.split()
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
