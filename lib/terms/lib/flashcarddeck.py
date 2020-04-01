#This file does not have to deal with reading data from disk so it does not need read jssl

#assumes that data is in the form of lists of tuples

import random
class Deck ():
    def __init__(self, deck=[]):
        '''
        Saves the list of cards to a variable
        '''
        self.deck = []
        self.addCards(deck)
    #methods
    def addCard (self, card):
        '''
        If card is (key,value) card is added to self.deck
        '''
        if type(card) != type(()) or len(card) != 2:
            raise TypeError("card paramater for add card method must be tuple of lenth 2")
        #add card        
        try:
            #only add card if it isn't in the deck
            self.deck.index(card)

        except:
            self.deck.append(card)


    def addCards (self, cards):
        try:
            assert type(cards) == type([])
        except:
            raise TypeError("cards parameter for addCards method must be list")
        #add cards
        for card in cards:
            self.addCard(card)

    def readtop (self):
        if not self.empty():
            return self.deck[0]
        else:
            return ("Deck Empty", "Deck Empty")

    def toptoback (self):
        if not self.empty():
            top = self.deck.pop(0)
            self.deck.append(top)

    def removecard(self,card):
        try:
            self.deck.remove(card) 
        except:
            pass

    def empty(self):
        isempty = len(self.deck) == 0
        return isempty 

    def shuffle(self):
        random.shuffle(self.deck) 
    
