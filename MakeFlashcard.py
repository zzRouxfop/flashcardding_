from CommaManagement import *
import os 

import random
import string

def synth(question, a, b, c, d): #synthesizes user input (question + 4 choices) into a flashcard
    InitialFlashcard = [question, a, b, c, d] 
    FinalFlashcard = commaconverter(InitialFlashcard)
    print("question added!")
    FinalFlashcard = ",".join(FinalFlashcard)
    return FinalFlashcard

def compile(flashcard_list, flashcard_txt_doc):
    for element in flashcard_list:
        flashcard_txt_doc.write(element + ",\n") #compiles the flashcards into a set/flashcard deck

def make_flashcard():
    titular = str(input("flashdeck title:")).strip().lower()
    title = 'flashdecks/' + titular + '.txt'
    AllFlashcards = []
    #making title for flashcard, variable AllFlashcards is a list of the question (0th element), correct answer (1st element), and the other choices (rest of the list)

    closeFlashcard_Captcha = ''
    for i in range(5):
        closeFlashcard_Captcha += random.choice(string.ascii_lowercase)
        # captcha thing so that the user doesn't get asked if they are finished with their flashdeck 

    with open(title, "w") as file:
        while True: 
            question = str(input(f"question (type in {closeFlashcard_Captcha} to close flashdeck): "))

            if closeFlashcard_Captcha == question:
                compile(AllFlashcards, file)
                print(f"flashdeck {titular} finished!")
                break
            
            a = str(input("choice 1 (CORRECT ANSWER): "))
            b = str(input("choice 2: "))
            c = str(input("choice 3: "))
            d = str(input("choice 4: "))
            #inputting question and four choices
            #if the user input of the variable {question} is the same as the variable {closeflashcard_captcha}, the flashdeck closes

            AllFlashcards.append(synth(question, a, b, c, d))
            #turning the question and four choices into a flashcard



            '''
            CloseFlashcard = str(input("would you like to close this flashcard set? [Y/N]: "))
            CloseFlashcard = CloseFlashcard.strip().lower()
            if CloseFlashcard == "n":
                continue
            elif CloseFlashcard == "y":
                compile(AllFlashcards, file)
                print("flashcard set", title, "all done!")
                break
            '''
            #asks the user whether he is finished with making the set of flashcards (DEPRECATED)

if __name__ == "__main__":
    make_flashcard()