def synth(a, b, c, d, question):
    #making row
    row = [question, a, b, c, d]
    #choosing which choice is correct
    CorrectAnswer = str(input("which choice was the correct answer? [A/B/C/D]: "))
    CorrectAnswer = CorrectAnswer.lower().strip()
    #putting correct choice on the second item on the list {row}
    if CorrectAnswer == "b":
        row.remove(b)
        row.insert(1, b)
    elif CorrectAnswer == "c":
        row.remove(c)
        row.insert(1, c)
    elif CorrectAnswer == "d":
        row.remove(d)
        row.insert(1, d)
    #final confirmation
    print(row, "added!")
    #output
    row = ",".join(row)
    return row


