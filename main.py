from datetime import datetime, timedelta

import calendar
import time
import os
import pytz

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

# Example usage
sol_5()

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

# Example usage
sol_6()