from MakingFlashcardSet import *

title = str(input("flashcards title:"))
file = open(title + ".txt", "w")
while True:
    question = str(input("question: "))
    a = str(input("choice A: "))
    b = str(input("choice B: "))
    c = str(input("choice C: "))
    d = str(input("choice D: "))
    file.write(synth(a, b, c, d, question)) #this bit of code is a bit buggy, will work on it later