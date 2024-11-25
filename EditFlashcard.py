from CommaManagement import *
from filefinder import *

import random
import string

def editflashcard():
    printAllFlashdecks()
    title = str(input("which flashcard set would you like to edit?: "))
    f = 'flashdecks/' + title + ".txt"
    finalFlashdeck = [] #collects all the flashcards together
    try:
        with open(f) as file: #reading the file
            for flashcard in file: #for every flashcard, it will be processed by the block of code under this line
                flashcard = khmerconverter(flashcard) #processes any possible commas in Q+4Cs
                flashcard_dictionary = {
                    "question": flashcard[0],
                    "A": flashcard[1],
                    "B": flashcard[2],
                    "C": flashcard[3],
                    "D": flashcard[4]
                }

                for element in flashcard_dictionary:
                    print(element, " | ", flashcard_dictionary[element])

                inputting = str(input((f"what part of the flashcard would you like to edit? [Q/A/B/C/D] \ntype [N] to go to continue to next flashcard\ntype [R] to remove flashcard from flashdeck\nnote: it's recommended to edit [Q] or [A]\ntype the choices as a string (i.e. \"qabc\" to edit the question, a, b, and c): ")))
                # what part of the flashcard would you like to edit? [Q/A/B/C/D] 
                # type [N] to continue to next flashcard
                # type [R] to remove flashcard from flashdeck
                # note: it's recommended to edit [Q] or [A]
                # type the choices as a string (i.e. "qabc" to edit the question, a, b, and c): 

                inputting = inputting.strip().upper()
                stuffToEdit = list(inputting)
                
                if 'R' in inputting:
                    continue
                if 'N' in inputting: 
                    finalFlashdeck.append([flashcard_dictionary['question'], flashcard_dictionary['A'], flashcard_dictionary['B'], flashcard_dictionary['C'], flashcard_dictionary['D']])
                    continue
                #lets user skip to the next flashcard if this flashcard doesn't need any editing
                
                elif 'Q' in stuffToEdit:
                    stuffToEdit.remove('Q')
                    stuffToEdit.insert(0, 'question')
                #tweakin the list like how i'm tweakin out rn xwx

                for l in stuffToEdit: #actual fucking editing YIPPEEEEE
                    print(f"editing {flashcard} | {flashcard_dictionary[l]} (choice \'{l})\'")
                    inputting = str(input('new input: '))
                    flashcard_dictionary[l] = inputting

                finalFlashdeck.append([flashcard_dictionary['question'], flashcard_dictionary['A'], flashcard_dictionary['B'], flashcard_dictionary['C'], flashcard_dictionary['D']])

        inputting = str(input(f"would you like to add new flashcards to {title}? [Y/N]"))

        if inputting == 'y':
            additions = []

            closeFlashcard_Captcha = ''
            for i in range(5):
                closeFlashcard_Captcha += random.choice(string.ascii_lowercase)
            # captcha thing so that the user doesn't get asked if they are finished with their flashdeck 

            while True:
                question = str(input(f"question (type in {closeFlashcard_Captcha} to close flashdeck): "))

                if closeFlashcard_Captcha == question:
                    break
                
                a = str(input("choice 1 (CORRECT ANSWER): "))
                b = str(input("choice 2: "))
                c = str(input("choice 3: "))
                d = str(input("choice 4: "))

                listing = [question, a, b, c, d]
                listing = commaconverter(listing)
                listing = ','.join(listing)
                additions.append(listing)
            #adding new stuff to flashcard

        elif inputting == 'n':
            pass

        with open(f, 'w') as file:
            finalFlashdeck = [commaconverter(element) for element in finalFlashdeck]
            finalFlashdeck = [','.join(element) for element in finalFlashdeck]
            for element in finalFlashdeck:
                decoration = khmerconverter(element)
                print(f"writing {decoration[0]}...")
                element += ',\n'
                file.write(element)
            for element in additions:
                decoration = khmerconverter(element)
                print(f"writing {decoration[0]}...")
                element += ',\n'
                file.write(element)
        #re-writing the file with the revised flashcards

        print("done!")

    except FileNotFoundError:
        print(f"{title} not found!")
            


if __name__ == "__main__":
    editflashcard()