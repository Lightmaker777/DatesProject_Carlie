from datetime import datetime

import calendar
import time
import os
import pytz

#Converting a string to a datetime object
datetime_string= '09/19/22 13:55:26'
# convert datetime string to datetime object
datetime_object = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')

print(datetime_object)