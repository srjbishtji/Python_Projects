# The great part of creating your own GUI apps is that you can customize them however you want. From text font to background colour, all features are available for customization. I will create a digital clock with Python.

# Digital Clock with Python
#  This is a simple task to get started with the Tkinter library in Python, which is a built-in package that comes with Python. Tkinter has some cool features that can be used to build simple apps.

from tkinter import Label, Tk
import time


# Now let’s define the title and size of our application. Note that in the code below I will set both the height and width of the resizable function as True(1,1) if you want a fixed window and don’t want to maximize or minimize the output you can set it to False(0,0):

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

# Now here I will define the font of the time and its colour, its border width and the background colour of the digital clock:

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

# Now here I will combine all the elements to define the label of the clock application:

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

# Now let’s define the main function of our digital clock. Here I will set the text of the label as the realtime:

def digital_clock(): 
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()



# Complete Code : 

# from tkinter import Label, Tk 
# import time
# app_window = Tk() 
# app_window.title("Digital Clock") 
# app_window.geometry("420x150") 
# app_window.resizable(1,1)

# text_font= ("Boulder", 68, 'bold')
# background = "#f2e750"
# foreground= "#363529"
# border_width = 25

# label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
# label.grid(row=0, column=1)

# def digital_clock(): 
#     time_live = time.strftime("%H:%M:%S")
#     label.config(text=time_live) 
#     label.after(200, digital_clock)

# digital_clock()
# app_window.mainloop()