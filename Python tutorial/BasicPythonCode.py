from datetime import date

#To print 5 times what we have in quotes marks
print ('Enrique, ' * 5)

# Ask to the user for input

#name=input('What\'s your name? ')
#print('Nice to meet you ',name)

#Parse a value to be able to work with it,
#use of date class and the type function

#year=input('Year of birth: ')
#print(type(year))
#age =  date.today().year - int(year)
#print('Your age is near ',age)

#Get some caracters from a string 
string='This is an example string'
print(string[0]) #Show T
print(string[-1]) #Show g, the last letter
print(string[:4]) #Show This
print(string[11:]) #Show example string
print(string[11:-2]) #Show example stri

#Formatted strings
form ='formatted'
str= 'string'
msn= f'Example of a {form} [{str}] in python'
print(msn)

#Some String methods
ex='Example text'
print(ex.upper())#Show the string in uppercase
print(len(ex))#Show the number of characters
print(ex.lower())#Show the string in lowercase
print(ex.replace('text','using replace method'))#Replace the first value for the second one 
print(ex.find('E'))#Show the index of the character (-1 if is not in it)
print('Example' in ex)#Return a boolean value
print(ex.title())#Set the first character in uppercase

#Operators
x=10
x += 3 #That way we add,mul,sub,.. a variable 
x ** 3 #Exponentiation a variable

#Math functions
import math
x=2.9
print(round(x)) #Show the variable round (3 in this case)
print(abs(-2.9)) #Return value in positive
print(-abs(x)) #Return value in negative
print(math.floor(x)) #Show the low round of the variable 

#Small practice (Guess game)
#n=7
#lives=3
#while lives != 0:
#    
#    userGuess=int(input('Guess a number: '))
#    lives -=1
#    if (userGuess==n):
#        print('Congrats, you guessed it!!')
#        break
#    elif (lives == 0):
 #       print('Sorry you lost!!')
#        break

#For loop
for item in 'Pyton': #Print each letter
    print(item) 

for item in ['Pyton','Java','JavaScript','C#']: #Print each element
    print(item) 

for item in range(0,10): #Print the numbers from 0 to 9
    print(item)

for item in range(0,10,2): #Print the numbers from 0 to 9 stepping 2
    print(item)

prices=[5,7,6,33]
value=0
for item in prices:
    value = value + item
print(f'The total value is: {value}')    

#Loop practice
numbers=[5,2,5,2,2]
for count in numbers: #Print the numbers from 0 to 9 stepping 2
    print('X' * count)

#List practice, get the largest number in a list
numbers=[5,7,1,8,3,66,55,88,4,1,99,100]
largest=0
pos=0
neg=-abs(len(numbers))
#print(neg+ 1)
#for num in numbers[0:math.floor(len(numbers)/2)]:
for num in numbers:
    print(num)
    if numbers[pos] > numbers[neg]:
        largest=numbers[pos]
    else:
        largest=numbers[neg]
    pos +=1
    neg +=1
print(f'The largest number is : {largest}')

#2D list
matrix =[[1,2,3],[4,5,6],[7,8,9]]
for list in matrix:
    print(list)#Show each list in the matrix[1,2,3],...
    for num in list:
        print(num)#Show each number of the matrix list 1,2,3,4,5...

#List methods
#numbers=[5,7,1,8,3,66,55,88,4,1,99,100]
#numbers.reverse() #Turn the list values around
#print(numbers)
#numbers.append(13) #Put the number at the end of out list
#numbers.insert(0,7) #We choose where put the new value (index,newValue)
#numbers.remove(13) #Delete the number of our list
#numbers.clear() #delete all the values
#numbers.pop() #delete the last value
#numbers.index(1) #Show the first occurrence of this value (error if is not in the list)
#50 in numbers #True o false, no error like index
#numbers.count(1) #Return how many times it is the value in our list
#numbers.sort() #Sort the values in ascending order 
#numbers.copy() #Copy our list 

#Practice: Remove the duplicates of a list
numbers=[6,5,7,1,8,7,5,8,4,1,5,1]
no_reps=[]
for num in numbers:
    if num not in no_reps:
       no_reps.append(num)
print(f'The list without duplicates is: {no_reps}')

#Tuples, normally use to avoid changes of the data inside
numbers=(1,2,3) #Tuples use () not [ ]

#Unpacking, works with list too "[]"
coordinates=(1,2,3)
x,y,z=coordinates #Each variable get a value from the tupla
print(x) #Return 1

#Dictionaries (Key value)
customer = {
    "name":"Enrique",
    "surname":"Barca",
    "age":30,
    "verified":True
}
print(customer['name'])#Return Enrique, if there is no key give a error
customer['name']= 'Oscar'#Updating the value of a key
customer['sex']='Male'#Setting a new key and value
print(customer['name'])#Return Enrique, if there is no key give a error
print(customer.get('name'))#.get return none if the key does not exist
print(customer.get('birth_year',1991))#With .get we can use a default value

#Practice, transform digits in number letters
customer = {
    0:"Cero ",
    1:"One ",
    2:"two ",
    3:"Trhee ",
    4:"Four ",
    5:"Five ",
    6:"Six ",
    7:"Seven ",
    8:"Eight ",
    9:"Nine "
}
number=input('What\'s yout phone number?')
letters_phone=""
for num in number:
    i=int(num)
    letters_phone=letters_phone + customer.get(i)
print(letters_phone)

#Functions
def number_to_letters(number):

    customer = {
        0:"Cero ",
        1:"One ",
        2:"two ",
        3:"Trhee ",
        4:"Four ",
        5:"Five ",
        6:"Six ",
        7:"Seven ",
        8:"Eight ",
        9:"Nine "
    }
    letters_phone=""
    for num in number:
        i=int(num)
        letters_phone=letters_phone + customer.get(i)
    print(letters_phone)

number_to_letters(input('What\'s yout phone number?'))

#Function using key value argument, could be useful to improve the readability of our code
def say_hello(first_name,last_name):
    print(f'Hello {first_name} {last_name}')
    print('Welcome to Python!')

say_hello(last_name='Barca',first_name='Enrique')#Return Hello Enrique Barca
say_hello('Barca',first_name='Enrique')#If we mix first it has to be the positional and them the keyword argumet

#Function with return
def square(number):
    return number*number

print(square(3))#Return 9

#
#
#
#
#
#
#