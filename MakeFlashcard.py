import random

def synth(a, b, c, d, question): #synthesizes user input (question + 4 choices) into a flashcard
    row = [question, a, b, c, d] 

    CorrectAnswer = str(input("which choice was the correct answer? [A/B/C/D]: "))
    CorrectAnswer = CorrectAnswer.lower().strip()

    if CorrectAnswer == "b":
        row.remove(b)
        row.insert(1, b)
    elif CorrectAnswer == "c":
        row.remove(c)
        row.insert(1, c)
    elif CorrectAnswer == "d":
        row.remove(d)
        row.insert(1, d)

    print(row[0], "added!")

    row = ",".join(row)
    return row

def compile(flashcard_list, flashcard_txt_doc):
    for element in flashcard_list:
        flashcard_txt_doc.write(element + ",\n") #compiles the flashcards into a set/flashcard deck

def make_flashcard():
    title = str(input("flashcard set title:"))
    title = title.strip().lower()
    AllFlashcards = []
    #making title for flashcard, variable AllFlashcards is a list of the question (0th element), correct answer (1st element), and the other choices (rest of the list)

    file = open(title + ".txt", "w") #opening file


    while True: 
        question = str(input("question: "))
        a = str(input("choice A: "))
        b = str(input("choice B: "))
        c = str(input("choice C: "))
        d = str(input("choice D: "))
        #inputting question and four choices

        AllFlashcards.append(synth(a, b, c, d, question))
        #turning the question and four choices into a flashcard

        CloseFlashcard = str(input("would you like to close this flashcard set? [Y/N]: "))
        CloseFlashcard = CloseFlashcard.strip().lower()
        if CloseFlashcard == "n":
            continue
        elif CloseFlashcard == "y":
            compile(AllFlashcards, file)
            break
    print("flashcard set", title, "all done!")
    file.close()
    #asks the user whether he is finished with making the set of flashcards

if __name__ == "__main__":
    make_flashcard()