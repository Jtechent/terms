import sys
from flashcarddeck import Deck
from cardflipview import DeckFlipView
from os import listdir


def controller(view, jssl, jassler,kill):
        #kill flag for ending the program
        #read data into program
        terms = jassler.read(jssl)

        #create command user command handlers

        def change_decks(x):
            '''
            input  --> str x
                command string passed from user
            output --> str
                string informing user of swap
            '''
            first_term = terms.pop(0)
            terms.append(first_term)
            return f"Swapped out deck for next one available"


        #card operations start

        def next_card(x):
            '''
            input  --> str x
                command string passed from user
            output --> str k in 1st (k,v) in terms[0] after terms[0].toptoback()
            '''
            terms[0].toptoback()
            return display_term(x)

        def flip_card(x):
            '''
            input  --> str x
                command string passed from user
            output --> str
                string containing v in 1st (k,v) in terms[0]
            '''
            return f"Definition: {terms[0].readtop()[1].upper()}"
        
        def display_term(x):
            '''
            input  --> string x
                command string passed from user
            output --> str
                string containing k in 1st (k,v) in terms[0] in uppercase
            '''
            return f"Term: {terms[0].readtop()[0].upper()}"

        def discard(x):
            #pop card out of deck, move value into the back of the deck at i=1 
            card = terms[0].readtop() 
            terms[0].removecard(card)#TODO: blug likely here
            terms[1].addCard(card)
            return "Term moved out of deck"
        #card operations end


        def shuffle(x):
            terms[0].shuffle()
            return "Cards Shuffled"
        def merge_decks(x):
            terms = [terms[0].addCards(terms[1].deck), Deck([('label','b')])]
        def quit(x):
            kill['kill'] = True 
            jassler.write(terms, jssl)
            return "Goodbye!"

        #hook up for view
        known_commands = {
            'c': change_decks,
            'n': next_card,
            'r': display_term,
            'f': flip_card,
            'd': discard,
            's': shuffle,
            'm': merge_decks,
            'q': quit 
        }
        def default_mapping (x):
            return f"Unknown command {x}"

        def string2function_mapper_gen (mapping, default):
            '''
            input  --> dict mapping, func default
                dict mapping
                    dict form    {string key: func value,}
                    func default default function returned where no mapping found
            output --> func mapper
                func mapping
                    input -->  str string
                    output --> result of mapping[string]()
            '''
            def mapper(string):
                return mapping.get(string, default)(string)
            return mapper 
        #create UI
        DeckFlipView(string2function_mapper_gen(known_commands, default_mapping), kill)
        
