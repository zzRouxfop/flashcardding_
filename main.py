from MakingFlashcardSet import *

title = str(input("flashcards title:"))
file = open(title + ".txt", "w")

question = str(input("question: "))
a = str(input("choice A: "))
b = str(input("choice B: "))
c = str(input("choice C: "))
d = str(input("choice D: "))
file.write(str(synth(a, b, c, d, question)))
file.close()