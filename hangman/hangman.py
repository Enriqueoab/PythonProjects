import random
import string
import re
#That way we can get the resources which we create on the words document (The words array)
from words import words

def getWord(words):
    #Ramdomly we get a word from the list
    choseWord=random.choice(words)
    #This loop make sure that the word hasn't any other caracter but letters
    while re.search('^[a-zA-Z]+$',choseWord) is None:
        choseWord=random.choice(words)

    return choseWord.upper()

def hangman():
    
    choseWord=getWord(words)

    #Using set we store just the differents letters of the word
    wordLetters=set(choseWord)
    usedLetters=set()
    alphabet = set(string.ascii_uppercase)
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
                elif userLetter == choseWord:
                    print("Congratulations you guess the word!!")
                    endGame=True
        else:
            print(f"You already try the letter {userLetter}")        

hangman()