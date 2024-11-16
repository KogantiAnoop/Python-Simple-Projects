#Typing Speed game
'''Unlike most typing speed games(Monkey Type, Type Racer, etc), This code is implemented to obtain 
the typing speed by getting the amount of correct letters clicked divided by the average of typical word sizes(4.6)'''

import random
from graphics import *
import time


def random_line(filename):
    with open(filename) as f:
        lines = f.readlines()                   #find a random line to get words from
        return random.choice(lines).strip()

def getSent(senSize):
    sentence = ""
    while senSize != 0:
        sentence += random_line("1000-most-common-words.txt") + " " #Get the sentence size in words
        senSize -= 1    
    return sentence[:-1]

def getSize(sentence,senSize):
    avgSize = 0
    sen = sentence.split()        #get the length of the sentence in letters 
    for word in sen:
        avgSize += len(word)
    return avgSize +  + ( senSize - 1)
    

def main():
    win = GraphWin("Typing Speed Game", 600, 400) 
    win.setBackground("white")
    
   
    instructions = Text(Point(300, 50), "Enter the number of words for your sentence:")
    instructions.setSize(14)                 # Instruction Label for the game
    instructions.draw(win)
    
    
    lengthEntry = Entry(Point(300, 100), 10)
    lengthEntry.draw(win)      # Input button for sentence length
    
    
    confirmButton = Text(Point(300, 150), "Click to Generate Sentence")
    confirmButton.setSize(12)       # pauses code to wait for the user to click to confirm through this built button
    confirmButton.draw(win)
    
    
    win.getMouse()
    
    # Get sentence length input from the person running the program
    try:
        senSize = int(lengthEntry.getText())
        while senSize <= 0:
            senSize = int(lengthEntry.getText())
    except:
        errorMsg = Text(Point(300, 200), "Invalid input. Please click anywhere and restart the game.")
        errorMsg.setFill("red")
        errorMsg.draw(win)
        win.getMouse()
        win.close()
    
    
    instructions.undraw()
    lengthEntry.undraw() # clean out the window and generate the sentence
    confirmButton.undraw()
    
    sentence = getSent(senSize)
    
    
    senText = Text(Point(300, 100), sentence)
    senText.setSize(14)   # Display the sentence 
    senText.draw(win)
    
    
    typingEntry = Entry(Point(300, 200), 50)
    typingEntry.draw(win)   # design the input box where the text written by person is shown
    
    start_time = time.time()


    while True:
        user_input = typingEntry.getText().strip()

        
        if user_input == sentence:
            end_time = time.time() # Check if the input matches the sentence perfectly and then end timer if true
            break
        win.update() #System before this couldnt handle updating properly causing it to crash. This helps update it consistently.
    
    
    elapsedTime = round(end_time - start_time, 2)
    letters = getSize(sentence,senSize)
    avgWordLen = 4.6                                            #calculated results usingamount of letters(including spaces) and dividing by wordlength and elapsed time in minutes
    wpm = round((letters) / avgWordLen / (elapsedTime / 60), 2)
    
    
    senText.undraw() # Window reset to show the results 
    typingEntry.undraw()
    
    results = f"Time: {elapsedTime}s\nWPM: {wpm}"
    resultsText = Text(Point(300, 200), results)
    resultsText.setSize(14)
    resultsText.draw(win)
    
    
    closeMsg = Text(Point(300, 350), "Click anywhere to close")
    closeMsg.setSize(12)        # Wait for the person to close the window
    closeMsg.draw(win)
    
    win.getMouse()
    win.close()


main()


