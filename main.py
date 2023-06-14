from datetime import datetime, timedelta

import calendar
import time
import os
import pytz

def sol_5(td):          # Ievgeniia
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
unit = sol_5(td)
print(f"Result: {unit}")

def sol_6(year=None, month=None):
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

# Input for new date
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

sol_6(year, month)

