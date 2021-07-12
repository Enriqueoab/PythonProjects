import random
import string
from words import words
#That way we can get the resources which we create on the words document (The words array)

def getWord(words):
#Ramdomly we get a word from the list
    choosedWord=random.choice(words)
    
    return choosedWord.upper()

def hangman():
    
    choosedWord=getWord(words)

    #Using set we store just the differents letters of the word
    wordLetters=set(choosedWord)
    usedLetters=set()
    #userLetter=input("Guess a letter").upper
    endGame=False
    
    while len(wordLetters) > 0:
       
        print(" ".join(usedLetters))
        userLetter=input("Guess a letter: ").upper
        if userLetter not in usedLetters:
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                if len(wordLetters)==0:
                    print("Congratulations you guess the word!!")
                    endGame=True
                if userLetter not in wordLetters:
                    usedLetters.add(userLetter)
                elif userLetter == choosedWord:
                    print("Congratulations you guess the word!!")
                    endGame=True
        else:
            print(f"You already try the letter {userLetter}")        

hangman()