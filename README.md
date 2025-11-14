# CS361-Random-Quotes-Generator
A microservice using ZeroMQ to communicate with a main program and print randomly chosen quotes.

# Instructions
Before using this microservice, the user will want to ensure they add a similar example call to their main program to allow connection between the client and server.

# Example Call in Main Program (In Python)
At the beginnging of your main program, you want to have the following import functions:
import zmq
import time

Then you want to have the following code block at the beginning of the main program:
context = zmq.Context()
print('Connecting...')

socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')


This code will be placed at the time of calling the microservice
#change the character value '1' to '2' or '3' for other types of quotes
#1 = positive
#2 = inspirational
#3 = motivational
socket.send_string('1') # should get a positive quote
message = socket.recv()


At the end of your main program, once you are done with communicating with the server, add this code block:
context.destroy()

#NOTE: context.destroy() will destroy ALL instances of zeroMQ connection, be careful with microservices running in tandem.


# Error Messages

 # Error: Main code did not append proper number to quote request. Try an int, 1-3
 Main program did not send the characters '1', '2', or '3'. 

 # Error: Message Received is not an integer
 String sent to microservice was not an integer value

 # UML
<img width="1960" height="960" alt="Screenshot 2025-11-14 141728" src="https://github.com/user-attachments/assets/f6a50f08-f9ab-4851-8e9c-a3cdb3bf2b46" />
