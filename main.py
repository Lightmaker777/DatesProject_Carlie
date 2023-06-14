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
    #Converting a string to a datetime object
    datetime_string = input("Enter a datetime in this format 'mm/dd/yy h:m:s': ")
    # convert datetime string to datetime object
    datetime_object = datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S')

    print(datetime_object)
    return 0

def sol_4():    #Hernan
    return 0

def sol_5():    #Ievgennia
    return 0

def sol_6():    #Ievgennia
    return 0

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