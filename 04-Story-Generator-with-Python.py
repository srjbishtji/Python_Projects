# Do you think the most complex use of the random module in Python is random sampling? No, we can also generate random stories or anything beyond that using the random module.

# Our task is to generate a random story every time the user runs the program. I will first store the parts of the stories in different lists, then the Random module can be used to select the random parts of the story stored in different lists.


# Code :

import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))



# I first imported the random module and then I created parts of the stories in different lists, then I only selected the parts of the lists at random to generate a random story.