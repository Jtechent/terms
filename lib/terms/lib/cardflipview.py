import os

def DeckFlipView(controller, kill):
    '''
    input --> func controller, obj kill
            func controller
                provides a way to pass user commands to the controller
            obj kill
                contains key "kill" and when true the view will close
    output --> void
    '''
    commands =  ['list of commands\n',
                'c: change decks\n',
                'n: next card\n',
                'f: flip card\n',
                'd: discard card to other deck\n',
                's: shuffle current deck\n',
                'm: merge decks\n',
                'q: quit this program\n']
    os.system('cls' if os.name == 'nt' else 'clear')
    commands = ''.join(commands)
    print("Current ",controller('r'))    
    while (kill['kill'] == False):
        user_input  = input(commands)
        os.system('cls' if os.name == 'nt' else 'clear')
        controller_response = controller(user_input) 
        print("Current ",controller('r'))    
        print("Command Result: ",controller_response)
