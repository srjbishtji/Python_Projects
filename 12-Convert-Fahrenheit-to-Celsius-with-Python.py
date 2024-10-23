# Most countries around the world use the Celsius scale to indicate temperatures, but the United States still uses the Fahrenheit scale.

# Calculating temperature conversion is simple. We have to convert the temperature because Celsius and Fahrenheit have different starting points; 0 degrees Celsius is 32 degrees Fahrenheit. So to convert Fahrenheit to degrees Celsius, we just need to subtract 32 from the temperature Fahrenheit.

# Sometimes the size of the units is also different. Celsius divides the temperature range between the freezing and boiling points of water is 100 degrees, while Fahrenheit divides this range into 180 degrees, so I will also multiply the value by 5/9 to convert 180 degrees into 100.

# Code :

def convert(f):
    celcius = (f-32)*(5/9)
    return celcius
fahrenheit = float(input("enter the temperature in celcius : "))
print(convert(fahrenheit))


# Code :

def converts(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
print(converts(78))