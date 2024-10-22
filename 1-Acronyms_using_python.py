# An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing.


# code :

user_input = input("Enter the Phrase : ")
text = user_input.split()
# print(text)
a = ""
for i in text:
    a += str(i[0]).upper()
print(a)


# In the above code, I am first taking a string user input, then I am using the split() function in Python for splitting the sentence. Then I declared a new variable ‘a’ to store the acronym of a phrase.