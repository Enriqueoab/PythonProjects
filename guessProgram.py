import random

# #That way we declare a function (def guess(lastNum))
# def weTryToGuess(lastNum):
#     random_num=random.randint(1,lastNum);
#     guess=0
#     while guess != random_num:
#         #We have to make sure that the time of variable is int
#         guess=int(input(f"Which number I am thinking of between 1 and {lastNum}? "))
#         if guess > random_num:
#             print("Too high, try again")
#         elif guess < random_num:
#             print("Too low, try again")
        
#     print("Great,That is the exact number")

# #In that point we call the function
# weTryToGuess(15)

def computerTryToGuess(lastNumber,ourNumber):
    computerGuess=random.randint(1,lastNumber)
    feedback=""

    while computerGuess != ourNumber:
        print(f"Bad computer,try again {computerGuess}")
        
        #That way we get some AI getting closer if the computer 
        # guess too high or too low 
        if  computerGuess > ourNumber:
            lastNumber=computerGuess
            computerGuess=random.randint(1,lastNumber-1)    
        elif  computerGuess < ourNumber:
            computerGuess=random.randint(computerGuess+1,lastNumber)   
        
    print(f"Good computer, you got it {computerGuess},{ourNumber}")

computerTryToGuess(50,35)