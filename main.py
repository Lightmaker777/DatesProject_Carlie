from datetime import datetime

import calendar
import time
import os
import pytz

#Converting a string to a datetime object
datetime_string = input("Enter a datetime in this format 'mm/dd/yy h:m:s': ")
# convert datetime string to datetime object
datetime_object = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')

print(datetime_object)