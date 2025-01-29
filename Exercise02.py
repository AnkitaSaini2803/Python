# If-else program                                     4/1/2025

# Create a python program capable of greeting you with Good Morning, 
# Good Afternoon and Good Evening. Your program should use time module 
# to get the current hour.

import time
timing=time.strftime("%H:%M:%S")
print(timing)

current_hour=int(time.strftime('%H'))
print(current_hour)

minute=int(time.strftime('%M'))
print(minute)

second=int(time.strftime('%S'))
print(second)

if(current_hour < 12):
    print('Good Morning')
elif(current_hour>=12 and current_hour<=15):
    print("Good Afternoon")
elif(current_hour<=18):
    print("Good evening")
else:
    print("Good night")