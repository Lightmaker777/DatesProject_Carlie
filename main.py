from datetime import datetime, timedelta

import calendar
import time
import os
import pytz

# Output a timedelta object with options to display only seconds, only days,
# or only years. Create a function that accepts a timedelta object and 
# provides options to extract specific units (seconds, days, or years) from it. 
# Allow users to choose which unit they want to display.

'''def extract_timedelta_units(td):
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

# Example usage
td = timedelta(days=500, seconds=3600)
unit = extract_timedelta_units(td)
print(f"Result: {unit}")'''

#----------------------------------------------------------------------------------------------------

# Print a calendar for the current month or a specified month.
# Use the calendar module or external libraries to generate a calendar 
# for the current month or a month specified by the user. 
# Ensure the calendar is displayed in a clear and readable format.

def print_calendar(year=None, month=None):
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

# Example usage
print_calendar()  # Print calendar for the current month and year

# Alternatively, specify a different year and month
#print_calendar(year=2023, month=6)
