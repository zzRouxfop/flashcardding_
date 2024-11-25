#principle: if the question or any one of the four choices has a comma, the comma 
# will be replaced with ឣ (a deprecated khmer character) to prevent bugs when the affected flashdeck is used for quizzing

def commaconverter(row):
    FinalFlashcard = [] # build final flashcard with processed commas
    for element in row: #processes [q, a, b, c, d] by their elements
        stringing = list(element) #turns each element (i.e. "example") into ["e", "x", "a", "m", "p", "l", "e"]

        Counter = 0 
        for element_ in stringing:
            if element_ == ",":
                stringing.pop(Counter)
                stringing.insert(Counter, "ឣ")
            Counter += 1
        #goes thorugh every element in stringing and does the principle

        FinalFlashcard.append("".join(stringing))
    return FinalFlashcard
    #adds processed element to the final flashcard and treats it as output
    #inputs list and outputs string

def khmerconverter(flashcard):
    InitialFlashcard = flashcard.split(",")
    FinalFlashcard = [] # build final flashcard with processed commas
    for element in InitialFlashcard: #processes [q, a, b, c, d] by their elements
        stringing = list(element) #turns each element (i.e. "example") into ["e", "x", "a", "m", "p", "l", "e"]

        Counter = 0 
        for element_ in stringing:
            if element_ == "ឣ":
                stringing.pop(Counter)
                stringing.insert(Counter, ",")
            Counter += 1
        #goes thorugh every element in stringing and does the principle

        FinalFlashcard.append("".join(stringing))

    FinalFlashcard.pop(-1) #remove newline
    return FinalFlashcard
    #adds processed element to the final flashcard and treats it as output
    #inputs string and outputs newline