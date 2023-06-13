from datetime import datetime

import calendar
import time
import os
import pytz

def clear_scr():
    # Clear screen command based on the operating system
    if os.name == 'posix':  # For UNIX and Linux systems (e.g., macOS, Linux)
        _ = os.system('clear')
    elif os.name == 'nt':  # For Windows systems
        _ = os.system('cls')

    
def get_option():               #prints the menu and returns an option

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
        print('10: : Surprise feature of your choice')
        print('\n"EXIT" for exiting the program')
        
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
    return 0

def sol_2():    #Marouan
    return 0

def sol_3():    #Gloria
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

def sol_5():    #Ievgennia
    return 0

def sol_6():    #Ievgennia
    return 0

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
    return 0

def sol_9():    #Alex
    return 0

def sol_10():   #Gloria
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
