# It’s great to develop an app that reminds you of your plans like an alarm or a to-do list.

# How Does a Desktop Notification App Work?
# The main purpose of the desktop notification app that you will learn to develop today is to constantly remind us of the different things that we need to accomplish throughout the day.

# This task is similar to a to-do list, where we have a set of goals to achieve. And the desktop notification app will constantly notify us of the different to-do and actions to take throughout the day.

# Desktop Notification with Python

# I am going to create a desktop notification app to get a reminder to rest after every hour. Your message and alert can be absolutely anything you want. You can have a list of things you need to do in the day, week or month, and the reminder app will constantly remind you of the same.

# For this task you need to install a Python library known as Plyer, which is used to access the hardware components of your system. This library can be easily installed by using the pip command; pip install pyler.


# Code :

import time 
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a Break !! It's been an hour.",
            timeout = 10
        )
        time.sleep(3600)


# After running the code, you will continuously receive notifications every hour or until the time you set due to the while loop defined in the code.