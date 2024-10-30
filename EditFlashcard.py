from CommaManagement import *

def EditFlashcard():
    f = str(input("which flashcard deck would you like to edit?: ")) + ".txt"
    with open(f) as file:
        for flashcard in file:
            question = khmerconverter(flashcard)
            for element in question:
                print(element)
                



if __name__ == "__main__":
    EditFlashcard()