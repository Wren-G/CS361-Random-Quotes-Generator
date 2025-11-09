#This file will contain the main implementation of the random quote microservice
#Assumed data given: a string with a character/integer appended to the front 
# to determine what type of quote the user is requesting

#libraries go here
import random

#global quote variable
quote = ""

#Functions

#This is a random number generator to generate a number between 1-10
def randomNumGen():
    return random.randint(1, 10)


#This function holds all the positive theme quotes
def positiveQuote():
    quoteNum = randomNumGen
    if (firstNum == 1):
        quote = ""
    elif (firstNum == 2):
        quote = ""
    elif (firstNum == 3):
        quote = ""
    elif (firstNum == 4):
        quote = ""
    elif (firstNum == 5):
        quote = ""
    elif (firstNum == 6):
        quote = ""
    elif (firstNum == 7):
        quote = ""
    elif (firstNum == 8):
        quote = ""
    elif (firstNum == 9):
        quote = ""
    else:
        quote = ""
    #options for end of function:
    #return quote potentially
    # OR
    #print(quote)

#This function holds all the inspirational theme quotes
def inspirationalQuote():
    quoteNum = randomNumGen
    if (firstNum == 1):
        quote = ""
    elif (firstNum == 2):
        quote = ""
    elif (firstNum == 3):
        quote = ""
    elif (firstNum == 4):
        quote = ""
    elif (firstNum == 5):
        quote = ""
    elif (firstNum == 6):
        quote = ""
    elif (firstNum == 7):
        quote = ""
    elif (firstNum == 8):
        quote = ""
    elif (firstNum == 9):
        quote = ""
    else:
        quote = ""
    #options for end of function:
    #return quote potentially
    # OR
    #print(quote)

#This function holds all the motivational theme quotes
def motivationalQuote():
    quoteNum = randomNumGen
    if (firstNum == 1):
        quote = ""
    elif (firstNum == 2):
        quote = ""
    elif (firstNum == 3):
        quote = ""
    elif (firstNum == 4):
        quote = ""
    elif (firstNum == 5):
        quote = ""
    elif (firstNum == 6):
        quote = ""
    elif (firstNum == 7):
        quote = ""
    elif (firstNum == 8):
        quote = ""
    elif (firstNum == 9):
        quote = ""
    else:
        quote = ""
    #options for end of function:
    #return quote potentially
    # OR
    #print(quote)




#Main program
firstNum = 0 #get first character of string from zeroMQ

if (firstNum == 1):
    positiveQuote()
elif (firstNum == 2):
    inspirationalQuote()
elif (firstNum == 3):
    motivationalQuote()
else:
    print("Error: Main code did not append proper number to quote request")