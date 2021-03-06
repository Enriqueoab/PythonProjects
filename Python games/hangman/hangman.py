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
    
    choseWord = getWord(words)

    #Using set we store just the differents letters of the word
    wordLetters = set(choseWord)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 6 

    while len(wordLetters) > 0 and lives > 0:
       #Show the letters already used
                                    #join turns the iterable(usedLetters)
                                    #into a string separated by what .join has
                                    #before the dot(A space in this case)
        print('You have ',lives,' lives left and you have used these letters: ', ' '.join(usedLetters))

        #Show the word's letters already guess
        wordList = [letter if letter in usedLetters else '-' for letter in choseWord]
        print('Current word: ', ' '.join(wordList))

        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives=lives-1
                print(f'The letter {userLetter} in not in the word')

        elif userLetter in usedLetters:
            print(f'You already try the letter {userLetter}')

        else:
            print('Invalid character. Please try again')   
    #Getting out the loop with a result (Win o loose)
    if lives==0:
        print('You lost, the word was: ', choseWord)
    else:
        print('You guessed the word: ', choseWord,' congratulations!!')


hangman()