# -----------------------------------------------------------------------------------------------------------
# random_quotes.py
# Project: CS361 Random Quotes Generator
# Purpose: ZeroMQ REP microservice that returns a random quote based on a category id
#          (1 = POSITIVE, 2 = INSPIRATIONAL, 3 = MOTIVATIONAL).
# Authors: Katherine Collier, Logan Moskal, Wren Gilbert
# Date: 2025-11-21
# Usage: Run `python random_quotes.py`. Client sends a single integer (1-3) as the request;
#        the service responds with a quote string.
# -----------------------------------------------------------------------------------------------------------

import random
import zmq
import time


# DATA STRUCTURES (Fixes Long Function and Long Lines)
# defined constants to fix vague naming 
POSITIVE = 1
INSPIRATIONAL = 2
MOTIVATIONAL = 3


QUOTES = {
    POSITIVE: [
        "This too shall pass.",
        "This moment is not something happening to you, it is something you are making every moment, with every thought.",
        "You are growing, you are changing, but remember that one day you wished to be where you are right now.",
        "You don't have to control your thoughts. You just have to stop letting them control you. — Dan Millman",
        "The greatest weapon against stress is our ability to choose one thought over another. — William James",
        "Between stimulus and response, there is a space. In that space is our power "
        "to choose our response. In our response lies our growth and our freedom. — Viktor E. Frankl",
        "Criticizing yourself all the time or being judgmental of yourself is like wearing sunglasses indoors — Matthew McKay",
        "Tomorrow is a new day. You shall begin it serenely and with too high a spirit to be encumbered with your old nonsense. — Ralph Waldo Emerson",
        "In three words, I can summarize everything I've learned about life. It goes on. — Robert Frost",
        "Out of suffering have emerged the strongest souls; the most massive characters are seared with scars. — Khalil Gibran"
    ],
    INSPIRATIONAL: [
        "Spread love everywhere you go. Let no one ever come without leaving happier. — Mother Teresa",
        "It does not matter how slowly you go, as long as you do not stop. — Confucius",
        "You can be everything. You can be the infinite amount of things that people are. — Kesha",
        "Be the change that you wish to see in the world. — Mahatma Ghandi",
        "If my mind can conceive it, if my heart can believe it, then I can achieve it. — Muhammad Ali",
        "The people who are crazy enough to think they can change the world are the ones who do. — Steve Jobs",
        "Once you replace negative thoughts with positive ones, you'll start having positive results. — Willie Nelson",
        "Stay close to anything that makes you glad you are alive. — Hafez",
        "We can't help everyone, but everyone can help someone. — Ronald Reagan",
        "Life has got all those twists and turns. You've got to hold on tight and off you go. — Nicole Kidman"
    ],
    MOTIVATIONAL: [
        "You are stronger than you know!",
        "Practice makes perfect! Keep it up!",
        "Nothing is impossible. The word itself says I'm possible! — Audrey Hepburn",
        "Dreams do not come true just because you dream them. It's hard work that makes things happen. It's hard work that creates change. — Shonda Rhimes",
        "Life has no limitations, except the ones you make. — Les Brown",
        "The best way to get started is to quit talking and begin doing. — Walt Disney",
        "Someone is sitting in the shade today because someone planted a tree a long time ago. — Warren Buffett",
        "We will fail when we fail to try. — Rosa Parks",
        "You're braver than you believe, stronger than you seem, and smarter than you think. — A.A. Milne",
        "Happiness is not something readymade; it comes from your own actions. — The Dalai Lama"
    ]
}


def get_quote(category_id):
    """Retrieves a random quote from the specified category."""
    if category_id in QUOTES:
        return random.choice(QUOTES[category_id])
    else:
        return "Error: Message received is not in the quote request. Try an int, 1—3."



def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:5555')
    print('Microservice is running on port 5555...')

    try:
        # fixes critical bug where program would crash on exit
        while True:
            # wait for next request from client
            message = socket.recv()
            
            try:
                # fixes vague naming code smell
                category = int(message.decode())
                response = get_quote(category)
            except ValueError:
                response = "Error: Message received is not in the quote request. Try an int, 1—3."
            
            # send the response back to client
            time.sleep(3)
            socket.send_string(response)

    except KeyboardInterrupt:
        print("Shutting down microservice...")
    finally:
        # ensure proper cleanup of zmq context
        context.destroy()

if __name__ == "__main__":
    main()