from CommaManagement import *
import os 

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
    title = 'flashdecks/' + str(input("flashcard set title:")).strip().lower() + '.txt'
    AllFlashcards = []
    #making title for flashcard, variable AllFlashcards is a list of the question (0th element), correct answer (1st element), and the other choices (rest of the list)

    with open(title, "w") as file:
        while True: 
            question = str(input("question: "))
            a = str(input("choice 1 (CORRECT ANSWER): "))
            b = str(input("choice 2: "))
            c = str(input("choice 3: "))
            d = str(input("choice 4: "))
            #inputting question and four choices

            AllFlashcards.append(synth(question, a, b, c, d))
            #turning the question and four choices into a flashcard

            CloseFlashcard = str(input("would you like to close this flashcard set? [Y/N]: "))
            CloseFlashcard = CloseFlashcard.strip().lower()
            if CloseFlashcard == "n":
                continue
            elif CloseFlashcard == "y":
                compile(AllFlashcards, file)
                print("flashcard set", title, "all done!")
                break
            #asks the user whether he is finished with making the set of flashcards

if __name__ == "__main__":
    make_flashcard()