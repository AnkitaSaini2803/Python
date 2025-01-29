'''Write a python program which reminds you of drinking water every hour or two. 
Your program can either beep or send desktop notifications for a specific operating
system
'''
import os
import time
import ctypes
import pyttsx3

REPEAT_INTERVAL = 3600


engine = pyttsx3.init()

while True:
    
    engine.say("Hey Harry, drink water")
    engine.runAndWait()
    
   
    ctypes.windll.user32.MessageBoxW(0, "Hey Harry, Drink water", "Reminder", 0x40 | 0x1)
    
    
    time.sleep(REPEAT_INTERVAL)
