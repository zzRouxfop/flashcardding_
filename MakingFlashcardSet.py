def synth(title, a, b, c, d, question):
    while title == None:
        #making questions and the four choices
        question = str(input("question: "))
        a = str(input("choice A: "))
        b = str(input("choice B: "))
        c = str(input("choice C: "))
        d = str(input("choice D: "))
        row = list(question, a, b, c, d)
        #choosing which choice is correct
        CorrectAnswer = str(input("which choice was the correct answer? [A/B/C/D]: "))
        CorrectAnswer = CorrectAnswer.lower().strip()
