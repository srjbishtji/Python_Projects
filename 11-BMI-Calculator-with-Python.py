# The Body Mass Index or BMI is calculated from weight and height of a Person.

# BMI is a measure of relative weight based on an individual’s mass and height. Today, Body Mass Index is commonly used to classify people as underweight, overweight, and even with obesity. Also, it is adopted by countries to promote healthy eating.

# BMI can be considered as an alternative for direct measurements of body fat. Besides, BMI is an inexpensive and easy-to-perform method of screening for weight classes that may cause health problems.

# The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, then dividing the answer again by their height. Now let’s see how to create a BMI calculator with Python:

# Code :

Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your weight in kg: "))
Height = Height / 100
BMI = Weight / (Height * Height)
print("Your Body Mass Index is:", BMI)

if BMI > 0:
    if BMI <= 16:
        print("You are severely underweight")
    elif BMI <= 18.5:
        print("You are underweight")
    elif BMI <= 25:
        print("You are healthy")
    elif BMI <= 30:
        print("You are overweight")
    else:
        print("You are severely overweight")
else:
    print("Enter valid details")
