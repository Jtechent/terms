import sys
sys.path.append('./lib')
from cardflipview import DeckFlipView
from controller import controller as Controller
from os import listdir
import nojassle


#simple calling program rn
def main():
    deck  = [sys.argv[i] if i < len(sys.argv) else "default" for i in range(2)][1] 
    kill = {"kill": False}
    controller = Controller(DeckFlipView, deck, nojassle, kill)


#start up the loop
main()
