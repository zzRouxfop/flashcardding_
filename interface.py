from MakeFlashcard import *
from QuizFlashcard import *
from EditFlashcard import *
from filefinder import *
from DelFlashcard import *
import os

print("welcome to flashdeck!")
print("current flashdecks:")
printAllFlashdecks()
print('\n')
inputting = str(input("type [M] to make flashdeck\ntype [Q] to quiz yourself on a flashdeck\ntype [E] to edit an existing flashdeck\ntype [D] to delete a flashdeck\ntype [X] to exit\n\n>>> "))
inputting = inputting.strip().lower()

if inputting == 'm':
    make_flashcard()
elif inputting == 'q':
    quizzing()
elif inputting == 'e':
    editflashcard()
elif inputting == 'd':
    DelFlashcard()
elif inputting == 'x':
    exit()

with open('interface.py', 'r') as file:
    code = file.read()
    exec(code)