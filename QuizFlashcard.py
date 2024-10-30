import random
from CommaManagement import *

def CheckAnswer(choices, correct_answer): #if answer is correct, returns true
    guess = int(input("answer [1/2/3/4]: "))
    guess -= 1
    if choices[guess] == correct_answer:
        return True
    else:
        return False

def finalscore(score, QuestionCounter):
    percentage = str(round(score/QuestionCounter, 2) * 100) #calculate percentage
    score = int(score)
    QuestionCounter = int(QuestionCounter)
    score = str(score)
    QuestionCounter = str(QuestionCounter) #important to set both as int's before setting both to strings or else the variables will be "n.0" instead of "n"
    return "Final score: " + score + "/" + QuestionCounter + " (" + percentage + "%)"
    #displays final score

def quizzing():
    f = str(input("which flashcard set would you like to open?: ")) + ".txt"
    with open(f) as file: #reading the file
        QuestionCounter = 0 # counts questions
        score = 0 #learner's final score; only increases when he gets the question right
        for flashcard in file: #for every flashcard, it will be processed by the block of code under this line
            AnswerCounter = 0 #counter for the four choices
            question = khmerconverter(flashcard)
            question.pop(-1)
            #turns the flashcard into a list (question + 4 choices + newline character) and removes the newline character and slowly removes elements in the list

            print("• " + question[0])
            question.pop(0)
            QuestionCounter += 1
            #prints out the question from the flashcard and removes it from the list as well as keeping track of how many questions are in the flashcard set for scoring

            CorrectAnswer = question[0] #stores the correct answer in the flashcard
            choices = [] #important variable, used let the user choose choice via input; this list is required because we're slowly destroying the original list

            for i in range(len(question)):
                AnswerCounter += 1
                AnswerCounter = str(AnswerCounter)
                display = random.randint(0, len(question)-1)
                print(AnswerCounter, question[display])
                choices.append(question[display])
                question.pop(display)
                AnswerCounter = int(AnswerCounter)
                #randomly chooses one of the four choices and adds it to the "choices" list and removes it from the original list
            
            if CheckAnswer(choices, CorrectAnswer) == True:
                score += 1

    score = float(score)
    QuestionCounter = float(QuestionCounter)
    print(finalscore(score, QuestionCounter))

if __name__ == "__main__":
    quizzing()