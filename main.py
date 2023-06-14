from datetime import datetime, timedelta

import calendar
import time
import os
import pytz
import random

#Globals
last_joke = None

def clear_scr():
    # Clear screen command based on the operating system
    if os.name == 'posix':  # For UNIX and Linux systems (e.g., macOS, Linux)
        _ = os.system('clear')
    elif os.name == 'nt':  # For Windows systems
        _ = os.system('cls')

    
def get_option():                #prints the menu and returns an option

    option = ' '
    quit = False
    while quit != True:
        clear_scr()
        print('Python-project-dates')
        print('MENU:\n')
        print('1.  : Display the current time')
        print('2.  : Display the current time in UNIX format')
        print('3.  : Convert a string to a datetime ')
        print('4.  : Check if the current year is a leap year ')
        print('5.  : Output a timedelta object ')
        print('6.  : Print a calendar for the current month or a specified month')
        print('7.  : Multinational team / Time Zone selection')
        print('8.  : Determine and display the current time at the opposite end of the world')
        print('9.  : Output a random joke from a predefined collection')
        print('10. : Surprise feature of your choice')
        print('\n"exit" for exiting the program')
        
        option = input('Select an option:').lower()

        if option =='exit':
            quit = True
        elif option not in ['1','2','3','4','5','6','7','8','9','10']:
            input('Please chose a valid option. Press ENTER to continue...')
        else:
            quit = True
        
    return option

#solutions for each problem here

def sol_1():    #Alex
    # Get the current time
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    print("Current time:", formatted_time)
    return 0

def sol_2():    #Marouan
    dt = datetime.now()
    print(dt)
    seconds = time.time()
    print("Seconds since epoch =", seconds)
    return 0

def sol_3():    #Gloria
    #Converting a string to a datetime object
    datetime_string = input("Enter a datetime in this format 'mm/dd/yy h:m:s': ")
    # convert datetime string to datetime object
    datetime_object = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')

    print(datetime_object) 
    return 0

def sol_4():    #Hernan

    current_year = datetime.now().year

    if calendar.isleap(current_year):
        print(f"{current_year} is a leap year.\n")
    else:
        print(f"{current_year} is not a leap year.\n")

    next_leap_year = current_year
    while not calendar.isleap(next_leap_year):
        next_leap_year += 1
    
    time_remaining = datetime(next_leap_year, 1, 1) - datetime.now()
    print(f"Time remaining until the next leap year: {time_remaining.days} days.\n")

    return 0

def sol_5():            # Ievgeniia
    # Prompt the user to input the values for days, hours, and minutes
    days = int(input("Enter the number of days: "))
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))

    # Create the timedelta object based on the user input
    time_delta = timedelta(days=days, hours=hours, minutes=minutes)

    # Define the choices for unit extraction
    choices = {
        "1": ("Seconds:", time_delta.total_seconds()),      # Option 1: Total seconds in timedelta
        "2": ("Days:", time_delta.days),                     # Option 2: Number of days in timedelta
        "3": ("Years:", time_delta.days // 365)              # Option 3: Approximate number of years in timedelta
    }
    
    while True:
        # Display the available unit options
        print("Choose the unit you want to display:")
        print("1. Seconds")
        print("2. Days")
        print("3. Years")
        choice = input("Enter your choice (1-3): ")

        if choice in choices:
            unit, value = choices[choice]
            print(f"{unit} {value}")    # Print the selected unit and its corresponding value
            break
        else:
            print("Invalid choice. Please try again.")


def sol_6():      # Ievgeniia
    # Get the current year and month
    year = calendar.datetime.datetime.now().year
    month = calendar.datetime.datetime.now().month

    # Generate the calendar matrix for the specified year and month
    cal = calendar.monthcalendar(year, month)

    # Get month name and year as strings
    month_name = calendar.month_name[month]
    year_str = str(year)

    # Print the calendar header
    print(f"Calendar for {month_name} {year_str}")
    print(calendar.weekheader(3))  # Display weekday abbreviations (e.g., Mon, Tue, etc.)

    # Print each day in the calendar matrix
    for week in cal:
        print(" ".join(f"{day:2d}" if day != 0 else "  " for day in week))


def sol_7():    #Hernan

    print('Your team is a multinational one meeting a regional leader based in Tokyo, Japan with the following regions:')
    print('[1] Tokyo/ Japan')
    print('[2] Dublin / Ireland')
    print('[3] San Francisco / USA')
    print('[4] Berlin / Germany')
    print('[5] Johannesburg / South Africa\n')

    time_zone = input('Select a time zone to check its time:')

    if time_zone in ['1','2','3','4','5']:
  
        if time_zone == '1':
            target_timezone = pytz.timezone('Asia/Tokyo')
            print('Time zone selected: Tokyo / Japan') 
        elif time_zone == '2':
            target_timezone = pytz.timezone('Europe/Dublin')
            print('Time zone selected: Dublin / Ireland')  
        elif time_zone == '3':
            target_timezone = pytz.timezone('America/Los_Angeles')
            print('Time zone selected: San Francisco / USA')  
        elif time_zone == '4':
            target_timezone = pytz.timezone('Europe/Berlin')
            print('Time zone selected: Berlin / Germany') 
        elif time_zone == '5':
            target_timezone = pytz.timezone('Africa/Johannesburg')
            print('Time zone selected: Johannesburg / South Africa ') 

        local_time = datetime.now()
        target_time = local_time.astimezone(target_timezone)
        formatted_time = target_time.strftime('%Y-%m-%d %H:%M')

        print(f'Current time: {formatted_time}\n')
    else:
        print('Time zone is not valid. Press ENTER to continue...')

    return 0

def sol_8():    #Marouan
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
    return 0

def sol_9():    #Alex

    global  last_joke

    jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What's the difference between a snowman and a snowwoman? Snowballs.",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call a bear with no teeth? A gummy bear!"
    ]

    random_joke = random.choice(jokes)
    
    
    while random_joke == last_joke:
        random_joke = random.choice(jokes)
    
    last_joke = random_joke
    print(random_joke+'\n')

    return 0

def sol_10():   #Gloria
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
    month = input("Enter travel month: ").title()
    if Country == 'germany':
        if month in ('March', 'April', 'May'):
            season = 'spring'
            print(f"It will be {season} in {Country} by {month}. This is a good time to travel.")
        elif month in ('June','July', 'August'):
            season = 'summer'
            print(f"It will be {season} in {Country} by {month}. This is a good time to travel.")
        elif month in ( 'September', 'October', 'November'):
            season = 'autumn'
            print(f"It will be {season} in {Country} by {month}. It is just about winter, but you can manage.")
        else:
            season = 'winter'
            print(f"It will be {season} in {Country} by {month}. You may want to consider traveling with winter jacket. ")

    elif Country == 'australia':
        if month in ('March', 'April', 'May'):
            season = 'autumn'
            print(f"It will be {season} in {Country} by {month}. It is just about winter, but you can manage.")
        elif month in ('June','July', 'August'):
            season = 'winter'
            print(f"It will be {season} in {Country} by {month}. You may want to consider traveling with winter jacket. ")
        elif month in ( 'September', 'October', 'November'):
            season = 'spring'
            print(f"It will be {season} in {Country} by {month}. This is a good time to travel.")
        else:
            season = 'summer'
            print(f"It will be {season} in {Country} by {month}. This is a good time to travel.")
        
    else:
        print("The country of your choice is not among the options")
    return 0


#main program

command = get_option()

while command != 'exit':

    clear_scr()

    if command == '1':
        sol_1()
    elif command == '2':
        sol_2()
    elif command == '3':
        sol_3()
    elif command == '4':
        sol_4()
    elif command == '5':
        sol_5()
    elif command == '6':
        sol_6()
    elif command == '7':
        sol_7()
    elif command == '8':
        sol_8()
    elif command == '9':
        sol_9()
    elif command == '10':
        sol_10()
   
    input('Press ENTER to continue...')
    command = get_option()

#end main program
