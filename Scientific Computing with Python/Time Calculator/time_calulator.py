# Defining a function called get_days_later() that takes in a single argument, days.
def get_days_later(days):
    """ Format the days later into string""" # Returns a string that represents the number of days later specified by the days argument.
    if days == 1: #  If days is 1, the function returns the string "(next day)"
        return "(next day)"
    elif days > 1: # If days is greater than 1, the function returns a string that includes the number of days followed by the string "days later"
        return f"({days} days later)"
    return "" # If days is 0 or negative, the function returns an empty string.

# Defining a function called add_time() that takes in three arguments: start_time, end_time, and day.
def add_time(start_time, end_time, day=False): # The start_time and end_time arguments are strings that represent the start and end times of an event. The day argument is a Boolean value that specifies whether the event takes place on a weekday or a weekend day. If day is True, the event takes place on a weekday. If day is False, the event takes place on a weekend day.

    
    # Defining constants
    HOURS_IN_ONE_DAY = 24 # HOURS_IN_ONE_DAY is a constant that represents the number of hours in one day. Its value is 24.
    HOURS_IN_HALF_DAY = 12 # HOURS_IN_HALF_DAY is a constant that represents the number of hours in half a day. Its value is 12.
    WEEK_DAYS = [ # # WEEK_DAYS is a list of strings that represents the days of the week
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    
    #  It takes the start_time and end_time arguments, which are strings in the format "HH:MM AM/PM", and converts them to integers
    days_later = 0
    hours, mins = start_time.split(":") # Splitting the start_time string at the colon to separate the hours from the minutes
    mins, period = mins.split(" ") # It then splits the minutes string at the space to separate the minutes from the period (AM or PM), the resulting variables are hours, mins, and period
    end_time_hrs, end_time_mins = end_time.split(":") 

    # Clean time data
    # Converts the hours, mins, end_time_hrs, and end_time_mins variables to integers using the int() function
    hours = int(hours)  # start time hours
    mins = int(mins)  # start time minutes
    end_time_hrs = int(end_time_hrs)  # end time hours
    end_time_mins = int(end_time_mins)  # end time minutes
    period = period.strip().lower()  # AM or PM, removes any leading or trailing whitespace from the period string and converts it to lowercase using the strip() and lower() string methods, respectively.

    # Combines the hours and minutes from the start and end times by adding the hours and end_time_hrs variables and the mins and end_time_mins variables. The resulting values are stored in the total_hours and total_mins variables. 
    total_mins = mins + end_time_mins
    total_hours = hours + end_time_hrs
    

    # Checks if the total_mins variable is greater than or equal to 60, and if it is, it increments the total_hours variable by the number of hours equivalent to the excess minutes
    if total_mins >= 60:
        total_hours += int(total_mins / 60)
        total_mins = int(total_mins % 60)
    
    # Checks if either the end_time_hrs or end_time_mins variables are greater than 0. If either of them is, it performs several operations:
    if end_time_hrs or end_time_mins:
        # If `PM`, flip period to `AM` if hours over 12
        if period == "pm" and total_hours > HOURS_IN_HALF_DAY: # If the period variable is "pm" and the total_hours variable is greater than 12, it checks if the total_hours variable is greater than or equal to 24. If it is, it increments the days_later variable by 1.
            # if hours over 24hr then add  days
            if total_hours % HOURS_IN_ONE_DAY >= 1.0:
                days_later += 1
        
        #  It checks if the total_hours variable is greater than or equal to 24. If it is, it increments the days_later variable by the number of days equivalent to the excess hours. For example, if total_hours is 54, the days_later variable will be incremented by 2.
        if total_hours >= HOURS_IN_HALF_DAY:
            hours_left = total_hours / HOURS_IN_ONE_DAY
            days_later += int(hours_left)

            # e.g: 54hr / 24 = 2.25 days <-- append 2 days
            # e.g.: 36hr / 24 = 1.5 days <-- append 1 days
        
        # Enters a while loop that runs until the temp_hours variable is less than 12. Inside the loop, it flips the period variable between "am" and "pm" and subtracts 12 from the temp_hours variable each time it runs.
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

  
    # This code is the final part of the add_time() function. It calculates the number of remaining hours and minutes by taking the remainder of the total_hours and total_mins variables when divided by 12 and 60, respectively. If the remaining_hours variable is 0, it sets it to hours + 1.
    remaining_hours = int(total_hours % HOURS_IN_HALF_DAY) or hours + 1
    remaining_mins = int(total_mins % 60)

    # Format the results as a string in the format "HH:MM AM/PM" and stores it in the results variable
    results = f"{remaining_hours}:{remaining_mins:02} {period.upper()}"
    if day:  # add the day of the week to the results string
        day = day.strip().lower()
        selected_day = int((WEEK_DAYS.index(day) + days_later) % 7)
        current_day = WEEK_DAYS[selected_day]
        results += f", {current_day.title()} {get_days_later(days_later)}"

    else:  # If the day argument is False, it adds the number of days later to the results string.
        results = " ".join((results, get_days_later(days_later)))

    # Function returns the results string, with any leading or trailing whitespace stripped using the strip() string method.
    return results.strip()
