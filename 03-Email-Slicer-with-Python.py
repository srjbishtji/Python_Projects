# An Email slicer is a very useful program for separating the username and domain name of an email address. 

# To create an email slicer with Python, our task is to write a program that can retrieve the username and the domain name of the email. For example, look at the image below which shows the domain and username of “support@thecleverprogrammer.com”:

# support ----> username
# thecleverprogrammer.com ----> domain name

email = input("enter your email : ").strip()
domain_seprater = input("enter the domain separator : ")
username, domain_name = email.split(domain_seprater)
print(f"Username : {username}")
print(f"Domain_Name : {domain_name}")



email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)

# The code above is very simple and easy to understand. We take user input and use the strip function at the same time to remove white space if any. Then we are finding the index of ‘@’ symbol of the user input. Then we store the index into a variable known as domain_name to split the email into two parts; the user name and the domain.

# make the first code operatable for all special characters. 