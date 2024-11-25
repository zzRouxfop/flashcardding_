import os
from filefinder import *

#deleting flashcards nothing much

def DelFlashcard():
    printAllFlashdecks()
    inputting = str(input('which flashdeck would you like to delete?: '))
    f = 'flashdecks/' + inputting + '.txt'
    warnUser = str(input('are you sure? this action can\'t be undone! [Y/N]: '))

    if warnUser == 'n':
        pass
    elif warnUser == 'y':
        print(f"{inputting} deleted! ")
        os.remove(f)
        