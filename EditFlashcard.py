from CommaManagement import *

def editflashcard():
    f = str(input("which flashcard set would you like to edit?: ")) + ".txt"
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

            inputting = str(input((f"what part of the flashcard would you like to edit? [Q/A/B/C/D] \ntype [CONTINUE] to go to next flashcard\nnote: it's recommended to edit [Q] or [A]\ntype the choices as a string (i.e. \"qabc\" to edit the question, a, b, and c): ")))
            # what part of the flashcard would you like to edit? [Q/A/B/C/D] 
            # type [CONTINUE] to go to next flashcard
            # note: it's recommended to edit [Q] or [A]
            # type the choices as a string (i.e. "qabc" to edit the question, a, b, and c): 



if __name__ == "__main__":
    editflashcard()

            
