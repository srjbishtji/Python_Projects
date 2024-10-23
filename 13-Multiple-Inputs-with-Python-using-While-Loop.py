# The input() function of Python help us to give a user input while writing a program. But how to take multiple user inputs in the terminal? 

# Problem Statement for Taking Multiple User Inputs with Python:
# Suppose you are prompted to write a Python program that interacts with a user in a console window. You may be accepting input to send to a database, or reading numbers to use in a calculation.

# Whatever the purpose, you should code a loop that reads one or multiple user inputs from a user typing on a keyboard and prints a result for each. In other words, you have to write a classic print loop program.

# Code :

while True:
    reply = input("Enter Text : ").lower()
    if reply == "stop" : break
    print(reply)
    
# The code leverages the Python while loop, Python’s most general loop statement. The built-in input function is used here for general console input, it prints its optional argument string as a prompt, and returns the response entered by the user as a string.

# A single-line if statement that uses the special rule for nested blocks also appears here. The body of the if statement appears on the header row after the colon instead of being indented on a new row below.

# Finally, the Python break statement is used to exit from the while loop statement immediately. It simply jumps out of the while loop statement and the program continues after the loop. Without this exit statement, the while would loop forever, because its test is still true.