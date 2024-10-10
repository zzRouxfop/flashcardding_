from MakingFlashcardSet import *

title = str(input("flashcard set title:"))
file = open(title + ".txt", "w")
AllFlashcards = []

while True: 
    question = str(input("question: "))
    a = str(input("choice A: "))
    b = str(input("choice B: "))
    c = str(input("choice C: "))
    d = str(input("choice D: "))
    AllFlashcards.append(synth(a, b, c, d, question))
    CloseFlashcard = str(input("would you like to close this flashcard set? [Y/N]: "))
    CloseFlashcard = CloseFlashcard.strip().lower()
    if CloseFlashcard == "n":
        continue
    elif CloseFlashcard == "y":
        compile(AllFlashcards, file)
        break
print("flashcard set", title, "all done!")
file.close()
