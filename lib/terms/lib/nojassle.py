from readjssl import Chew_JSSL as chew
from readjssl import Spit_JSSL as spit
from flashcarddeck import Deck


def read(db):
    '''
    input --> directory name
    output --> list of Deck objects of length 2
    '''
    print("Looking for cards...\n")
    try:
        with open(f"decks/{db}/deck.jssl") as deck:
            print("...Cards found")
            cards = chew(deck, tuples=True)
            if len(cards) < 2:
                cards.append([])
            return [Deck(x) for x in cards]
            
    except:
        print("None found, creating from source...")
        with open(f"decks/{db}/deck.source.jssl") as deck:
            cards = chew(deck, tuples=True)
            if len(cards) < 2:
                cards.append([])
            print("...Done")
            return [Deck(x) for x in cards]


def write(data, db):
    '''
    input:
        data --> list(Deck obj,)
        db   --> directory
    output:
        void
    note:
        output to disk --> jssl file with at least 2 JSSLL
    '''
    #I have to change the deck objects to the format capatible with the spit func
    data = [dict(deck.deck) for deck in data]
    if len(data) < 2:
        data.append({})
    with open(f"decks/{db}/deck.jssl", "w") as data_file:
        JSSL = spit(data)
        print(f"Writing data...\n{JSSL}")
        data_file.write(JSSL)
        print("...done\n")

