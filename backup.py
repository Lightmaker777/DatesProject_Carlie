from datetime import datetime

import calendar
import time
import os
import pytz

# number 2

dt = datetime.now()
print(dt)
seconds = time.time()
print("Seconds since epoch =", seconds)	

#task 7

# Define timezones for Sydney and Berlin
SydneyTz = pytz.timezone('Australia/Sydney')
BerlinTz = pytz.timezone('Europe/Berlin')
# Get current datetime in each timezone
datetimeInSydney = datetime.now(SydneyTz)
datetimeInBerlin = datetime.now(BerlinTz)
# Print the current time in Sydney and Berlin
print("The current time in Sydney is:", datetimeInSydney.strftime('%H:%M:%S'))
print("The current time in Berlin is:", datetimeInBerlin.strftime('%H:%M:%S'))
# Calculate the offset between UTC and local time in each timezone
Sydney_offset = datetimeInSydney.utcoffset()
Berlin_offset = datetimeInBerlin.utcoffset()
# Calculate the time difference
time_diff = Sydney_offset - Berlin_offset
# Since time_diff is a timedelta object, we need to convert it to hours and minutes
time_diff_hours = time_diff.seconds // 3600
time_diff_minutes = (time_diff.seconds // 60) % 60
# Print the time difference
print("Time difference between Sydney and Berlin: %d hours, %d minutes" % (time_diff_hours, time_diff_minutes))

