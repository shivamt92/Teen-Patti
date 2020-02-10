
"""  TO CREATE A TEEN PATTI GAME   """

import random


class Player:

    def __init__(self):
        self._hand = Hand()

    def initialize_hand(self, arr):
        self._hand.initialize_hand(arr)
        return

    def getScore(self):
        return self._hand.getScore()

    def display(self):
        return str(self._hand)

    def gethandtype(self):
        return self._hand.type()


class Card:
    Suits = { 1:'Heart', 2:'Spade', 3:'Diamond', 4:'Club'}
    numbers = {14:'Ace', 2:2 ,3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:'Jack', 12: 'Queen',13: 'King'}

    def __init__(self,num,suit):
        if num in self.numbers:
            self._num = num
        else:
            print('Invalid Card Entry')

        if suit in self.Suits:
            self._suit = suit
        else:
            print('Invalid Suit Entry')

    def __str__(self):

        if self._num and self._suit:

            s = ' Card : ' + str(self.Suits[self._suit]) + '-'+ str(self.numbers[self._num])
            return s

    def __repr__(self):

        if self._num and self._suit:

            s = ' Card : ' + str(self.Suits[self._suit]) + '-'+ str(self.numbers[self._num])
            return s


class Deck:

    def __init__(self):
        self._deck = []
        self._remaining_card = 0
        self.initialize()

    def initialize(self):
        self._deck = []
        for i in range(1,5):
            for j in range(2,15):
                self._deck.append(Card(j,i))
        self.shuffle()

    def remaining_cards(self):
        return self._remaining_card

    def shuffle(self):
        random.shuffle(self._deck)
        return

    def display(self):
        # for i in range(len(self._deck)):
        #     print(self._deck[i])
        print(self._deck)

    def extract(self):
        self.shuffle()
        arr = self._deck[-3:]
        del self._deck[-3:]

        return arr

    def __len__(self):
        return len(self._deck)-self._remaining_card


class Hand:

    def __init__(self):
        self._hand = [None]*3

    def __repr__(self):

        return str(self._hand)

    def initialize_hand(self,arr):
        assert len(arr)==len(self._hand)

        for i in range(3):
            self._hand[i] = arr[i]

    def isPair(self):
        dic = {}
        for h in self._hand:
            if h._num not in dic:
                dic[h._num]=1
            else:
                dic[h._num]+=1
                if dic[h._num] ==2:
                    return (True,h._num)

        return (False,False)

    def isThreeofKind(self):
        if self._hand[0]._num == self._hand[1]._num and self._hand[1]._num == self._hand[0]._num:
            return (True,self._hand[0]._num)
        return (False,False)

    def isFlush(self):

        if self._hand[0]._suit == self._hand[1]._suit and self._hand[1]._suit == self._hand[0]._suit:
            return [True,self._hand[0]._suit]
        return [False,False]

    def isStraight(self):

        arr = []

        for h in self._hand:
            arr.append(h._num)

        arr.sort()

        if arr[1]==arr[0]+1 and arr[2]==arr[1]+1:
            return [True,arr[0]]

        return [False,False]

    def isStraightFlush(self):
        if self.isStraight()[0] and self.isFlush()[0]:
            return [True,self.isStraight()[1]]

        return [False,False]

    def getScore(self):

        if self.isStraightFlush()[0]: return 1000
        elif self.isFlush()[0]: return 900
        elif self.isStraight()[0]: return 800
        elif self.isPair()[0]: return 500
        else: return 0

    def type(self):
        if self.isStraightFlush()[0]: return 'STRAIGHT FLUSH'
        elif self.isFlush()[0]: return 'FLUSH'
        elif self.isStraight()[0]: return 'STRAIGHT'
        elif self.isPair()[0]: return 'PAIR'
        else: return 'HIGH CARD'




class Game:

    def __init__(self):
        self._player = Player()
        self._computer = Player()
        self.numplayers = 2
        self.Dealer = Dealer()
        self.play()

    def play(self):
        self.Dealer.shuffle_deck()
        self.Dealer.dispense(self._player,self._computer)

        s1 = self._player.getScore()
        s2 = self._computer.getScore()
        print(' HUMANS   - HAND  ', self._player.display())
        print(' MACHINES - HAND  ', self._computer.display())


        if s1>s2:
            print('                 HUMANS   -- WON  WITH A ',self._player.gethandtype(),'\n' )
        elif s2>s1:
            print('                 MACHINES -- WON  WITH A ',self._computer.gethandtype(),'\n')
        else:
            print('                      DRAW\n')

        return

class TeenPatti(Game):

    pass


class Dealer:

    def __init__(self):
        self.board = Board()

    def decide_blind(self):
        pass

    def dispense(self,*args):
        """
        :param *args: Players passed as arguments
        :returns dispenses hands to each player

        """

        for arg in args:
            Handarr = self.board.extract()
            arg.initialize_hand(Handarr)



    def shuffle_deck(self):
        self.board.shuffle_deck()
        pass


    def getscore(self):

        pass

    def transfer_pot_to_player(self):
        pass

    pass


class Board:

    def __init__(self):
        self._deck = Deck()
        self._pot = Pot()
        self._flop = []

    def display(self):
        pass

    def extract(self):
        """

        :return: a length three hand from the deck randomly. removing those cards from the deck
        """

        return self._deck.extract()

    def shuffle_deck(self):
        self._deck.initialize()
        self._deck.shuffle()


class Pot:
    def __init__(self):
        self._pot = 0

    pass


if __name__ == '__main__':
    for i in range(100):
        Game()