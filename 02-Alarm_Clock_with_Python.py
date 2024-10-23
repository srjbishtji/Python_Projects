# An alarm clock is a clock with a function that can be activated to ring at a time set in advance, used to wake someone up.

# I will be using the DateTime module in Python to create an alarm clock and the sound library in Python to play the alarm sound.

# The DateTime module comes preinstalled in the Python programming language so you can easily import it in your program. The playsound library can be easily installed by using a pip command; pip install playsound. 

# Before writing the program you should know that you also need an alarm tone which will ring at the time of the alarm. So you can download an alarm tune from "https://www.soundsnap.com/tags/alarm".

# Code :


from datetime import datetime
from playsound import playsound

# Taking alarm input in 12-hour format with AM/PM
alarm_time = input("Enter the time of the alarm to be set : H:MM:SS AM/PM\n")
alarm_hour = alarm_time[0:2].strip()  # Handles single-digit hours by stripping spaces
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()  # Ensures AM/PM are in uppercase
print("Setting Up alarm ...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")  # %I is for 12-hour format (01-12)
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")  # %p is for AM/PM

    # Check if the current time matches the alarm time
    if (alarm_period == current_period):
        if (alarm_hour == current_hour):
            if (alarm_minute == current_minutes):
                if (alarm_seconds == current_seconds):
                    print("Wake Up !!")
                    playsound("audio.wav")  # Ensure the correct path for the audio file
                    break



# The user input should be in a format of hours: minutes: and then seconds. You will start listening to the song as you will reach the time that has been set. To test your code set the time 2 or 3 minutes later from the time you are giving the user input.