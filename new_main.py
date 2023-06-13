from datetime import datetime, timedelta

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
    return 0

def sol_5(td):    #Ievgeniia
    # Dictionary mapping user's input to unit values
    choices = {
        "1": td.total_seconds(),          # Option 1: Total seconds in timedelta
        "2": td.days,                     # Option 2: Number of days in timedelta
        "3": td.days // 365               # Option 3: Approximate number of years in timedelta
    }

    while True:
        print("Choose the unit you want to display:")
        print("1. Seconds")
        print("2. Days")
        print("3. Years")
        choice = input("Enter your choice (1-3): ")

        if choice in choices:
            return choices[choice]         # Return the corresponding unit value            
        else:
            print("Invalid choice. Please try again.")
            return 0    

# Example usage
td = timedelta(days=500, seconds=3600)
unit = sol_5(td)
print(f"Result: {unit}")
    

def sol_6(year=None, month=None):    #Ievgeniia    
    # Get the current year and month if not provided
    if year is None:
        year = calendar.datetime.datetime.now().year
    if month is None:
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
        return 0

# Example usage
sol_6()  # Print calendar for the current month and year

# Alternatively, specify a different year and month
#sol_6(year=2023, month=6)


def sol_7():    #Hernan
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
