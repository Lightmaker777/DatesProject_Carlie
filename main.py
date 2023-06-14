
from datetime import datetime

import calendar
import time
import os
import pytz

# way number 1

dt = datetime.now()
print(dt)
seconds = time.time()
print("Seconds since epoch =", seconds)	

#task 2

SydneyTz = pytz.timezone("Australia/Sydney") 
timeInSydney = datetime.now(SydneyTz)
currentTimeInSydney = timeInSydney.strftime("%H:%M:%S")
print("The current time In Sydney is:", currentTimeInSydney)

BerlinTz = pytz.timezone("Europe/Berlin")
timeInBerlin = datetime.now(BerlinTz)
CurrentTimeInBerlin = timeInBerlin.strftime("%H:%M:%S")
print("the currentTime In Berlin is ", CurrentTimeInBerlin)

import datetime
import pytz
# Get the current time in Sydney
sydney_tz = pytz.timezone('Australia/Sydney')
sydney_time = datetime.datetime.now(sydney_tz)
# Get the current time in another location
other_tz = pytz.timezone('Europe/Berlin')
other_time = datetime.datetime.now(other_tz)
# Calculate time difference between Sydney and other location
time_diff = other_time - sydney_time
# Display the time difference
print("Time difference between Sydney and Berlin:", time_diff)
