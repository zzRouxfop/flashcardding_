from CommaManagement import *
from filefinder import *


def editflashcard():
    printAllFlashdecks()
    f = 'flashdecks/' + str(input("which flashcard set would you like to edit?: ")) + ".txt"
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

                inputting = str(input((f"what part of the flashcard would you like to edit? [Q/A/B/C/D] \ntype [N] to go to continue to next flashcard\nnote: it's recommended to edit [Q] or [A]\ntype the choices as a string (i.e. \"qabc\" to edit the question, a, b, and c): ")))
                # what part of the flashcard would you like to edit? [Q/A/B/C/D] 
                # type [N] to continue to next flashcard
                # note: it's recommended to edit [Q] or [A]
                # type the choices as a string (i.e. "qabc" to edit the question, a, b, and c): 

                inputting = inputting.strip().upper()
                stuffToEdit = list(inputting)
                
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

        with open(f, 'w') as file:
            finalFlashdeck = [commaconverter(element) for element in finalFlashdeck]
            finalFlashdeck = [','.join(element) for element in finalFlashdeck]
            for element in finalFlashdeck:
                print(f"writing {element}...")
                element += ',\n'
                file.write(element)
        #re-writing the file with the revised flashcards

        print("done!")

    except FileNotFoundError:
        print(f"{f} not found!")
            

if __name__ == "__main__":
    editflashcard()

            
