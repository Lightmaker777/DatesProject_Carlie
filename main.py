from datetime import datetime

import calendar
import time
import os
import pytz

#Task_01
import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print("Current time:", formatted_time)

#Task_02

import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What's the difference between a snowman and a snowwoman? Snowballs.",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call a bear with no teeth? A gummy bear!"
]

last_joke = None

def tell_joke():
    global last_joke
    random_joke = random.choice(jokes)
    
    
    while random_joke == last_joke:
        random_joke = random.choice(jokes)
    
    last_joke = random_joke
    print(random_joke)


tell_joke()

