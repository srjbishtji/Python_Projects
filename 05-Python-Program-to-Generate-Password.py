# To create a password with Python, we need to create a program that takes the length of the password and generates a random password of the same length.

import random 
passlength = int(input("Enter the length of the password : "))
keys = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_=+<,>.?/:;{[]}|"
a = "".join(random.sample(keys,passlength))
print(a)

# In the above code, I first imported the random module in Python, then I asked for user input for the length of the password. Then I stored the letters, numbers and special characters that I want to be considered while generating a password. Then I am doing a random sampling by joining the length of the password and the variable s, which will finally generate a random password.