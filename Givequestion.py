from Takequestion import *

question_file = open(file, "r")
question_prompt=[]
questions=[]

#calling out the question in the designated file
for question in question_file:
    question_prompt.append(question)

#assign each question to each correct answer
for i in range(len(question_prompt)):
    questions.append(Question(question_prompt[i], synth(a, b, c, d, question)))

#this will run the quizz
def run_quizz(question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" +str(score)+"/"+str(len(questions))+" correct")
