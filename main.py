from datetime import datetime

import calendar
import time
import os
import pytz
# import datetime
#Converting a string to a datetime object
datetime_string = input("Enter a datetime in this format 'mm/dd/yy h:m:s': ")
# convert datetime string to datetime object
datetime_object = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')

print(datetime_object) 

# comparing seasons between two countries: Germany and Australia 
Germany = print("""
In Germany, the four seasons and their months are:
    spring = 'March to May'
    summer = 'June to August'
    autumn = 'September to October'
    winter = 'December to February'
""")
Australia = print("""
In Australia, the four seasons and their months are:
    spring = 'September to November'
    summer = 'December to February'
    autumn = 'March to May'
    winter = 'June to August'
""")
print("You wish to travel to either of these two countries: Germany and Australia. \nAnd you want to know the best time to travel")

Country = input("Please enter country name: ").lower()
month = input("Enter travel month: ").lower()
if Country == 'germany':
    if month in ('March', 'April', 'May'):
        season = 'spring'
    elif month in ('June','July', 'August'):
        season = 'summer'
    elif month in ( 'September', 'October', 'November'):
        season = 'autumn'
    else:
        season = 'winter'
    print(f"It is currently {season} in {Country} ")

elif Country == 'australia':
    if month in ('March', 'April', 'May'):
        season = 'autumn'
    elif month in ('June','July', 'August'):
        season = 'winter'
    elif month in ( 'September', 'October', 'November'):
        season = 'spring'
    else:
        season = 'summer'
    print(f"It is currently {season} in {Country} ")
else:
    print("The country of your choice is not among the options")


