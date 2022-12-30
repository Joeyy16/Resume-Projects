"""
This code defines a function called get_days_later() that takes in a single argument, days.

The function returns a string that represents the number of days later specified by the days argument. If days is 1, the function returns the string "(next day)". If days is greater than 1, the function returns a string that includes the number of days followed by the string "days later". If days is 0 or negative, the function returns an empty string.
"""

def get_days_later(days):
    """ Format the days later into string"""
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""

"""
This code defines a function called add_time() that takes in three arguments: start_time, end_time, and day.

The start_time and end_time arguments are strings that represent the start and end times of an event. The day argument is a Boolean value that specifies whether the event takes place on a weekday or a weekend day. If day is True, the event takes place on a weekday. If day is False, the event takes place on a weekend day.

The function also defines several constants:

HOURS_IN_ONE_DAY is a constant that represents the number of hours in one day. Its value is 24.

HOURS_IN_HALF_DAY is a constant that represents the number of hours in half a day. Its value is 12.

WEEK_DAYS is a list of strings that represents the days of the week. Its elements are the strings "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", and "sunday".
"""

def add_time(start_time, end_time, day=False):
    
    # constants
    HOURS_IN_ONE_DAY = 24
    HOURS_IN_HALF_DAY = 12
    WEEK_DAYS = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    """
    This code is part of the add_time() function. It takes the start_time and end_time arguments, which are strings in the format "HH:MM AM/PM", and converts them to integers.

    The code starts by splitting the start_time string at the colon to separate the hours from the minutes. It then splits the minutes string at the space to separate the minutes from the period (AM or PM). The resulting variables are hours, mins, and period.

    The code then does the same thing for the end_time string, resulting in the variables end_time_hrs and end_time_mins.

    Next, the code converts the hours, mins, end_time_hrs, and end_time_mins variables to integers using the int() function. It also removes any leading or trailing whitespace from the period string and converts it to lowercase using the strip() and lower() string methods, respectively.

    Finally, the code combines the hours and minutes from the start and end times by adding the hours and end_time_hrs variables and the mins and end_time_mins variables. The resulting values are stored in the total_hours and total_mins variables. 
    """

    days_later = 0
    hours, mins = start_time.split(":")
    mins, period = mins.split(" ")
    end_time_hrs, end_time_mins = end_time.split(":")

    # Clean time data
    hours = int(hours)  # start time  hours
    mins = int(mins)  # start time  minutes
    end_time_hrs = int(end_time_hrs)  # end time hours
    end_time_mins = int(end_time_mins)  # end time minutes
    period = period.strip().lower()  # AM or PM

    # Combine start time and end time hrs and minutes
    total_mins = mins + end_time_mins
    total_hours = hours + end_time_hrs
    
    """
    This code is also part of the add_time() function. It checks if the total_mins variable is greater than or equal to 60, and if it is, it increments the total_hours variable by the number of hours equivalent to the excess minutes. For example, if total_mins is 70, the total_hours variable will be incremented by 1. The total_mins variable is then set to the remainder of the division of total_mins by 60. For example, if total_mins is 70, the total_mins variable will be set to 10.

    The code then checks if either the end_time_hrs or end_time_mins variables are greater than 0. If either of them is, it performs several operations:

    If the period variable is "pm" and the total_hours variable is greater than 12, it checks if the total_hours variable is greater than or equal to 24. If it is, it increments the days_later variable by 1.

    It checks if the total_hours variable is greater than or equal to 24. If it is, it increments the days_later variable by the number of days equivalent to the excess hours. For example, if total_hours is 54, the days_later variable will be incremented by 2.

    It enters a while loop that runs until the temp_hours variable is less than 12. Inside the loop, it flips the period variable between "am" and "pm" and subtracts 12 from the temp_hours variable each time it runs.

    It is not clear from this code snippet what the purpose of these operations is or how they relate to the add_time() function's overall behavior. More context would be needed to understand the function's behavior.
    """

    # Shift minutes to hour if minutes is over 60
    if total_mins >= 60:
        total_hours += int(total_mins / 60)
        total_mins = int(total_mins % 60)

    if end_time_hrs or end_time_mins:
        # If `PM`, flip period to `AM` if hours over 12
        if period == "pm" and total_hours > HOURS_IN_HALF_DAY:
            # if hours over 24hr then add  days
            if total_hours % HOURS_IN_ONE_DAY >= 1.0:
                days_later += 1

        if total_hours >= HOURS_IN_HALF_DAY:
            hours_left = total_hours / HOURS_IN_ONE_DAY
            days_later += int(hours_left)

            # e.g: 54hr / 24 = 2.25 days <-- append 2 days
            # e.g.: 36hr / 24 = 1.5 days <-- append 1 days

        temp_hours = total_hours
        while True:
            # Constantly reverse period until
            # total_hours are less than half a day
            if temp_hours < HOURS_IN_HALF_DAY:
                break
            if period == "am":
                period = "pm"
            else:
                period = "am"
            temp_hours -= HOURS_IN_HALF_DAY

    """
    Recalculate Hours and Minutes 
    
     Since we have already taken care of the days,
     we now need to calculate the hours remaining.
     This can be done by subtracting the remaining days(in hours) 
     from the total hours remaining 
        
        e.g. hrs % oneday -->  55hrs % 24 = 7 ---> 7 hours remaining
    """
    
    """
    This code is the final part of the add_time() function. It calculates the number of remaining hours and minutes by taking the remainder of the total_hours and total_mins variables when divided by 12 and 60, respectively. If the remaining_hours variable is 0, it sets it to hours + 1.

    Next, it formats the results as a string in the format "HH:MM AM/PM" and stores it in the results variable. If the day argument is True, it adds the day of the week to the results string. If the day argument is False, it adds the number of days later to the results string.

    Finally, the function returns the results string, with any leading or trailing whitespace stripped using the strip() string method.
    """
    remaining_hours = int(total_hours % HOURS_IN_HALF_DAY) or hours + 1
    remaining_mins = int(total_mins % 60)

    # Format the results
    results = f"{remaining_hours}:{remaining_mins:02} {period.upper()}"
    if day:  # add the day of the week
        day = day.strip().lower()
        selected_day = int((WEEK_DAYS.index(day) + days_later) % 7)
        current_day = WEEK_DAYS[selected_day]
        results += f", {current_day.title()} {get_days_later(days_later)}"

    else:  # add the days later
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()
