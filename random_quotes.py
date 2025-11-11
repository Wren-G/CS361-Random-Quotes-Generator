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
    if (quoteNum == 1):
        quote = "This too shall pass."
    elif (quoteNum == 2):
        quote = "This moment is not something happening to you, it is something you are making every moment, with every thought."
    elif (quoteNum == 3):
        quote = "You are growing, you are changing, but remember that one day you wished to be where you are right now."
    elif (quoteNum == 4):
        quote = "You don't have to control your thoughts. You just have to stop letting them control you. - Dan Millman"
    elif (quoteNum == 5):
        quote = "The greatest weapon against stress is our ability to choose one thought over another. - William James"
    elif (quoteNum == 6):
        quote = "Between stimulus and response, there is a space. In that space is our power to choose our response. In our response lies our growth and our freedom. - Viktor E. Frankl"
    elif (quoteNum == 7):
        quote = "Criticizing yourself all the time or being judgmental of yourself is like wearing sunglasses indoors - Matthew McKay"
    elif (quoteNum == 8):
        quote = "Tomorrow is a new day. You shall begin it serenely and with too high a spirit to be encumbered with your old nonsense. ―Ralph Waldo Emerson"
    elif (quoteNum == 9):
        quote = "In three words, I can summarize everything I’ve learned about life. It goes on. - Robert Frost"
    else:
        quote = "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars. - Khalil Gibran"
    return quote

#This function holds all the inspirational theme quotes
def inspirationalQuote():
    quoteNum = randomNumGen
    if (quoteNum == 1):
        quote = "Spread love everywhere you go. Let no one ever come without leaving happier. - Mother Teresa"
    elif (quoteNum == 2):
        quote = "It does not matter how slowly you go, as long as you do not stop. —Confucius"
    elif (quoteNum == 3):
        quote = "You can be everything. You can be the infinite amount of things that people are. —Kesha"
    elif (quoteNum == 4):
        quote = "Be the change that you wish to see in the world. —Mahatma Ghandi"
    elif (quoteNum == 5):
        quote = "If my mind can conceive it, if my heart can believe it, then I can achieve it. —Muhammad Ali"
    elif (quoteNum == 6):
        quote = "The people who are crazy enough to think they can change the world are the ones who do. —Steve Jobs"
    elif (quoteNum == 7):
        quote = "Once you replace negative thoughts with positive ones, you'll start having positive results. —Willie Nelson"
    elif (quoteNum == 8):
        quote = "Stay close to anything that makes you glad you are alive. —Hafez"
    elif (quoteNum == 9):
        quote = "We can't help everyone, but everyone can help someone. —Ronald Reagan"
    else:
        quote = "Life has got all those twists and turns. You’ve got to hold on tight and off you go. —Nicole Kidman"
    return quote

#This function holds all the motivational theme quotes
def motivationalQuote():
    quoteNum = randomNumGen
    if (quoteNum == 1):
        quote = "You are stronger than you know!"
    elif (quoteNum == 2):
        quote = "Practice makes perfect! Keep it up!"
    elif (quoteNum == 3):
        quote = "Nothing is impossible. The word itself says I'm possible! —Audrey Hepburn"
    elif (quoteNum == 4):
        quote = "Dreams do not come true just because you dream them. It’s hard work that makes things happen. It’s hard work that creates change. —Shonda Rhimes"
    elif (quoteNum == 5):
        quote = "Life has no limitations, except the ones you make. —Les Brown"
    elif (quoteNum == 6):
        quote = "The best way to get started is to quit talking and begin doing. - Walt Disney"
    elif (quoteNum == 7):
        quote = "Someone is sitting in the shade today because someone planted a tree a long time ago. - Warren Buffett"
    elif (quoteNum == 8):
        quote = "We will fail when we fail to try. —Rosa Parks"
    elif (quoteNum == 9):
        quote = "You’re braver than you believe, stronger than you seem, and smarter than you think. —A.A. Milne"
    else:
        quote = "Happiness is not something readymade; it comes from your own actions. —The Dalai Lama"
    return quote




#Main program
def main():
    firstNum = 0 #get first character of string from zeroMQ

    if (firstNum == 1): #1 == positive
        quote = positiveQuote()
    elif (firstNum == 2): #2 == inspirational
        quote = inspirationalQuote()
    elif (firstNum == 3): #3 == motivation
        quote = motivationalQuote()
    else:
        print("Error: Main code did not append proper number to quote request")

    #Send back quote string variable with ZeroMQ