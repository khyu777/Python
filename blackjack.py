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
        return False

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
            return False
            
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
        self.cards = [self.drawcards(), self.drawcards()]
        self.bank = 1000
        self.setcount() 

    def check(self):
        if self.count[0] > 21:
            print('\nYour hand: ', self.cards)
            print('You went over 21 and lost!')
            self.bank -= self.bid
            self.bankrupt()
            self.restart()
            game.counter = 0
            return False
 
    def spcheck(self, num):
        if self.count[num] > 21:
            print('\nYour hand: ', self.cards[num])
            print('You went over 21 and lost!')
            self.bank -= self.bid
            self.bankrupt()
            self.restart()
            game.counter = 0
            return False
      
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
            self.count[0] += self.cards[-1][0][1]
        else:
            self.count[0] += self.cards[-1][0]
    
    def sphit(self, num):
        self.cards[num].append(self.drawcards())
        if isinstance(self.cards[num][-1][0], list) == False:
            self.count[num] += self.cards[num][-1][0]
        else:
            self.count[num] += self.cards[num][-1][0][1]
    
    def stand(self):
        dealer.hit()
        dealer.check()
        print('\nYour hand: ', player.cards)
        print('Dealer\'s hand: ', dealer.cards)
        if self.count[0] > dealer.count:
            print('You won!')
            self.bank += self.bid
        elif self.count[0] == dealer.count:
            print('You tied!')
        else:
            print('You lost!')
            self.bank -= self.bid
            self.bankrupt()

    def spstand(self, num=0):
        dealer.hit()
        dealer.check()
        print('\nYour hand: ', self.cards[num])
        print('Dealer\'s hand: ', dealer.cards)
        if self.count[num] > dealer.count:
            print('You won!')
            self.bank += self.bid
        elif self.count[num] == dealer.count:
            print('You tied!')
        else:
            print('You lost!')
            self.bank -= self.bid
            self.bankrupt()

    def split(self):
        self.cards = [[self.cards[0]], [self.cards[1]]]
        self.count = [[],[]]
        for sublist in self.cards:
            sublist.append(self.drawcards())
        for i in range(2):
            if isinstance(self.cards[i][0][0], list) == True and isinstance(self.cards[i][1][0], list) == True:
                self.count[i] = self.cards[i][0][0][1] + self.cards[i][1][0][1]
            elif isinstance(self.cards[i][0][0], list) == True and isinstance(self.cards[i][1][0], list) == False:
                self.count[i] = self.cards[i][0][0][1] + self.cards[i][1][0]
            elif isinstance(self.cards[i][0][0], list) == False and isinstance(self.cards[i][1][0], list) == True:
                self.count[i] = self.cards[i][0][0] + self.cards[i][1][0][1]
            else:
                self.count[i] = self.cards[i][0][0] + self.cards[i][1][0]

    def setcount(self):
        if isinstance(self.cards[0][0], list) == True and isinstance(self.cards[1][0], list) == True:
            self.count = [self.cards[0][0][1] + self.cards[1][0][1]]
        elif isinstance(self.cards[0][0], list) == True and isinstance(self.cards[1][0], list) == False:
            self.count = [self.cards[0][0][1] + self.cards[1][0]]
        elif isinstance(self.cards[0][0], list) == False and isinstance(self.cards[1][0], list) == True:
            self.count = [self.cards[0][0] + self.cards[1][0][1]]
        else:
            self.count = [self.cards[0][0] + self.cards[1][0]]
            
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
    print('game start')
    print(player.cards)
    if game.counter == 0:
        player.checkA()
        dealer.setcount()
        player.setcount()
        game.counter += 1
    player.check()
    dealer.check() #how to stop these two from not restarting?
    answer = input('\nWhat would you like to do? (Hit, Stand, or Split) ').lower()
    if answer == 'hit':
        player.hit()
        player.check()
    elif answer == 'stand':
        print('stand')
        player.stand()
        game.counter = 0
        game.restart()
        print('stand end')
    elif answer == 'split':
        player.split()
        while True:
            print('split start')
            print('\nFirst: ', player.cards[0])
            print('Second: ', player.cards[1])
            if player.count[0] > 21 or player.count[1] > 21:
                print('You went over 21 and lost!')
                player.bank -= player.bid
                game.restart()
                break
            pc1 = input('What would you like to do for First? (Hit, Stand, or Split) ')
            if pc1.lower() == 'hit': #first split hit
                player.sphit(0)
                player.spcheck(0)
            elif pc1.lower() == 'stand': #first split stand
                pass
            pc2 = input('What would you like to do for Second? (Hit, Stand, or Split) ')        
            if pc2.lower() == 'hit': #second split hit
                player.sphit(1)
                player.spcheck(1)
            elif pc1.lower() == 'hit' and pc2.lower() == 'stand':
                pass
            elif pc1.lower() == 'stand' and pc2.lower() == 'stand': #second split stand
                player.spstand(0)
                player.spstand(1)
                game.restart()
                break
            else:
                print('Please enter Hit, Stand, or Split \n')
    else:
        print('Please enter Hit, Stand, or Split \n')
